from djongo import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField() 
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class ActiveBookManager(models.Manager):
    def get_query_set(self):
        return super(ActiveBookManager, self).get_query_set().filter(is_active=True)

class Author(models.Model):
    name = models.CharField( max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField( max_length=50)
    address = models.CharField( max_length=50)
    mail = models.CharField( max_length=50)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_year = models.IntegerField(null=True)
    num_of_page = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    sold = models.IntegerField(null=True)
    cover = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    objects = models.Manager()
    active = ActiveBookManager()
    def __str__(self):
        return f"{self.title}"
    

    
