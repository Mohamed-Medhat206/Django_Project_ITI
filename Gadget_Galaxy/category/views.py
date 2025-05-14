from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def cat_list(requset, id):
    objrepo = HttpResponse()
    objrepo.write(f'<h1>Category {id}</h1>')
    return objrepo

