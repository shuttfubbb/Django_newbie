from django.db import models 
from django.contrib.auth.models import User 

class SearchTerm(models.Model): 
    q= models.CharField(max_length=50) 
    search_date = models.DateTimeField(auto_now_add=True) 
    ip_address = models.GenericIPAddressField() 
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __unicode__(self): 
        return self.q 