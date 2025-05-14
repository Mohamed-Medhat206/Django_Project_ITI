from django.shortcuts import render
from django.http.response import HttpResponse

def pro_list(requset, id):
    objrepo = HttpResponse()
    objrepo.write(f'<h1>Product {id}</h1>')
    return objrepo


