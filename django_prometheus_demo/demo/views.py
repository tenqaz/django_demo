from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from demo.models import User, User2


def my_view(request):
    User(name="zhangsan", age=12, sex="male").save()
    return HttpResponse("hello")
