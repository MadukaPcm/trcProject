from django.db import models
from uaa.models import User
from asset.models import SpareTool
from django.core.validators import FileExtensionValidator
import uuid

class CategoryOne(models.Model): #eg- office,electric station,rolling stock,spare part, recommended [spare pard and assets]
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=255,blank=True,null=True)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_categoryOne")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_categryOne")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.name)
    
    
class Inventory(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    categoryOne = models.ForeignKey(CategoryOne, related_name='CategoryOne_inventory',on_delete=models.DO_NOTHING)
    spareTool = models.ForeignKey(SpareTool, related_name = 'SpareTool_inventry', on_delete=models.DO_NOTHING)
    serialNumber = models.CharField(max_length=100,blank=True,null=True)
    spareName = models.CharField(max_length=100,blank=True,null=True)
    costSpent = models.CharField(max_length=100,blank=True,null=True)
    totalPrice = models.CharField(max_length=100,blank=True,null=True)
    lifeSpan = models.CharField(max_length=100,blank=True,null=True)
    mtl = models.CharField(max_length=100,blank=True,null=True)  #maintenance time length.
    siteName = models.CharField(max_length=100,blank=True,null=True) #place placed. eng....Trc-posta.
    userManual = models.FileField(upload_to='userManual/inventory/', 
                                    validators=[FileExtensionValidator(
                                        allowed_extensions=['pdf','docx','ppt'])],
                                    null=True,blank=True)
    orderStatus = models.BooleanField(default=False)
    vendor = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField()
    iam = models.BooleanField(default=False) #is automatic schedule manteined
    maintenanceNumber = models.IntegerField(default=0)
    unit = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_inventory")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_inventry")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.serialNumber)



class TradesSetting(models.Model):  
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    maxTradeNumber = models.IntegerField()
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_tradesSetting")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_tradesSettings")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.maxTradeNumber)
    