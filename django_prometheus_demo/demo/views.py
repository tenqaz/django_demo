from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from demo.models import User
from django.core.cache import cache


def my_view(request):
    return HttpResponse("hello")


def my_view2(request):
    User(name="zhangsan", age=12, sex="male").save()
    return HttpResponse("hello")


def my_view3(request):
    cache.set("name", "zhangsan")
    return HttpResponse(cache.get("name"))
