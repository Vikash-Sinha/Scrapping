from django.db import models

# Create your models here.
class ScrappingData(models.Model):
    date = models.DateField(auto_now_add=True, null=True,blank=True)
    language = models.CharField(max_length=200,blank=True, null=True)
    plateform = models.CharField(max_length=200,blank= True,null=True)
    state = models.CharField(max_length=200,blank= True,null=True)
    influancer= models.CharField(max_length=200,blank= True,null=True)
    channel_name = models.CharField(max_length=200,blank= True,null=True)
    type = models.CharField(max_length=200,blank= True,null=True)
    link = models.CharField(max_length=200,blank= True,null=True)
    subscriber = models.CharField(max_length=200,blank= True,null=True)
    avg_view = models.CharField(max_length=200,blank= True,null=True)
    feature = models.CharField(max_length=200,blank= True,null=True)
    review = models.CharField(max_length=200,blank= True,null=True)
    pokar = models.CharField(max_length=200,blank= True,null=True)
    contact_no = models.CharField(max_length=200,blank= True,null=True)
    email_id = models.CharField(max_length=200,blank= True,null=True)