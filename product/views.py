from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, InvalidPage, EmptyPage 
from . import search 
from baitap1 import settings

def searchBook(request):
    q = request.GET.get('q', '') 

    try: 
        page = int(request.GET.get('page', 1)) 
    except ValueError: 
        page = 1 
    matching = search.products(q).get('products') 
    paginator = Paginator(matching, settings.PRODUCTS_PER_PAGE) 
    try: 
        results = paginator.page(page).object_list 
    except (InvalidPage, EmptyPage): 
        results = paginator.page(1).object_list
        
    data = [ProductSerializer(x).data for x in results]
    return data

@api_view(["GET"])
def bookSearchApi(request): 
    data = searchBook(request)
    return Response(data)

#CREATE
class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer

# READ
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # renderer_classes = [TemplateHTMLRenderer]
    
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response({'products': serializer.data}, template_name='blog_list.html')
    
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response({'products': serializer.data}, template_name='blog_detail.html')

# UPDATE
class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# DESTROY
class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
