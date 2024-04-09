from django.contrib import admin
from .models import Product, Category, Publisher, Author

# Register your models here.

# class ProductAdmin(admin.ModelAdmin): 
#     # #form = ProductAdminForm 
#     # # sets values for how the admin site lists your products  
#     # list_display = ('title', 'price') 
#     # list_display_links = ('title',)
#     # list_per_page = 50 
#     # search_fields = ['title', 'description'] 
#     # # sets up slug to be generated from product name 

# # registers your product model with the admin site 
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
