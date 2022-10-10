from rest_framework import viewsets
from .models import *
from .serializers import *
from django.core.cache import cache
import time
import redis

from rest_framework.response import Response

redis_instance = redis.StrictRedis(host='127.0.0.1', port=6379, db=1)

def log_db_queries ( f ) :
    from django.db import connection
    def new_f ( * args , ** kwargs ) :
        start_time = time.time()
        res = f ( * args , ** kwargs )
        print ( "\n\n" )
        print ( "-"*80 )
        print ("db queries log for %s:\n" % (f.__name__))
        print ( " TOTAL COUNT : % s " % len ( connection.queries ) )
        for q in connection.queries :
            print ("%s: %s\n" % (q["time"] , q["sql"]))
        end_time = time.time ()
        duration = end_time - start_time
        print ('\n Total time: {:.3f} ms'.format(duration * 1000.0))
        print ("-"*80)
        return res
    return new_f

class MusicianViewSet(viewsets.ModelViewSet):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()
    @log_db_queries
    def list(self, request):
        first_name = self.request.query_params.get('first_name')

        if first_name is not None:
            cache_key = 'name' + first_name
        else:
            cache_key = 'name'

        if cache_key in cache:
            print("redis")
            queryset = cache.get(cache_key)
            return Response(queryset)
        else:
            print('db')
            queryset = Musician.objects.all()
            if first_name is not None:
                queryset = queryset.filter(first_name__contains=first_name)
                
            serializer_class = MusicianSerializer(queryset, many=True)
            cache.set(cache_key , serializer_class.data, timeout=60*60)
            return Response(serializer_class.data)
        
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()