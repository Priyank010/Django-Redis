# Django-Redis

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Priyank010/Django-Redis.git
$ cd Django-Redis
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ pip install virtualenv
$ virtualenv MyFirstApp
$ MyFirstApp\scripts\activate
```

Install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Finally run the project:

```sh
(env)$ cd djangoRedis
(env)$ python manage.py runserver
```
## Description
Redis has been implemented in Django REST framework to implement cache memory in it. Here you can see the speed increment proof.

### Before

![alt text](https://miro.medium.com/max/1400/1*PV-SJWKxbviW7Bvg1KUnvg.webp)

### After

![alt text](https://miro.medium.com/max/1400/1*CoXo09HrsqWc2YoOoXfdHA.webp)

## Blog
I've written a thorough blog post here. If you're interested in learning more, have a look.

https://priyankdesai515.medium.com/make-your-django-rest-api-10-times-faster-with-redis-5736baedb271