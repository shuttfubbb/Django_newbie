from rest_framework import serializers
from .models import Product, Author, Publisher, Category

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = ['name', 'dob', 'address', 'email']
        fields = "__all__"
        
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        # fields = ['name', 'address', 'mail']
        fields = "__all__"
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = ['name', 'slug', 'description']
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Product
        # fields = ['title', 'author', 'publisher', 'categories', 'publish_year', 'num_of_page', 'price', 'stock', 'sold', 'cover', 'description']
        fields = "__all__"