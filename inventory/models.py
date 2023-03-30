from django.db import models
from uaa.models import User
from asset.models import SpareTool
from uaa.models import Department
from django.core.validators import FileExtensionValidator
import uuid
from datetime import date,timedelta

class CategoryOne(models.Model): #eg- office,electric station,rolling stock,spare part, recommended [spare pard and assets]
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_categoryOno', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    
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
    department = models.ForeignKey(Department, related_name='department_inventory', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    categoryOne = models.ForeignKey(CategoryOne, related_name='CategoryOne_inventory',on_delete=models.DO_NOTHING)
    spareTool = models.ForeignKey(SpareTool, related_name = 'SpareTool_inventry', on_delete=models.DO_NOTHING)
    serialNumber = models.CharField(max_length=100,blank=True,null=True)
    spareName = models.CharField(max_length=100,blank=True,null=True)
    totalPrice = models.CharField(max_length=100,blank=True,null=True)
    lifeSpan = models.CharField(max_length=100,blank=True,null=True)
    mtl = models.CharField(max_length=100,blank=True,null=True)  #maintenance time length.
    siteName = models.CharField(max_length=100,blank=True,null=True) #place placed. eng....Trc-posta.
    orderStatus = models.BooleanField(default=False)
    vendor = models.CharField(max_length=100,blank=True,null=True)
    iam = models.BooleanField(default=True) #is automatic schedule manteined
    maintenanceNumber = models.IntegerField(default=0)
    unit = models.IntegerField(default=0)
    lastMaintained = models.DateField(null=True, blank=True)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_inventory")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_inventry")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    @property
    def IsDueForM(self):
        return (date.today()-self.lastMaintained).days >= (self.mtl-3)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.serialNumber)



class TradesSetting(models.Model):  
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_tradesSetting', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    maxTradeNumber = models.IntegerField()
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_tradesSetting", null=True, blank=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_tradesSettings", null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.maxTradeNumber)
    