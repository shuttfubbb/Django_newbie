from django.shortcuts import render
from django.core.paginator import Paginator, InvalidPage, EmptyPage 
from . import search 
from product.views import bookSearchApi
from baitap1 import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers
from product.serializers import ProductSerializer
from product.views import bookSearchApi, searchBook
import requests
import json
@api_view(["GET"])
def bookSearchApi(request):
    q = request.GET.get('q', '') 
    url = 'http://127.0.0.1:8000/procducts/search?q=' + q
    
    response = requests.get(url).json()
    #response = searchBook(request)
    return Response(response)
