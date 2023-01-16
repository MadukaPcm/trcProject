from django.db import models
from uaa.models import User,Branch
from inventory.models import Inventory
from django.core.validators import FileExtensionValidator
import uuid

class MaintenanceSchedule(models.Model):  #this is maintenance order
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    branch = models.ForeignKey(Branch, related_name='branch_maintenanceSchedul',on_delete=models.DO_NOTHING)
    inventory = models.ForeignKey(Inventory, related_name='inventory_maintenanceSchedule',on_delete=models.DO_NOTHING)
    
    #work order details.
    description = models.TextField()
    overalDuration = models.CharField(max_length=100,blank=True,null=True)
    rdoc = models.DateField(auto_now_add=True) #raisedDateOrderCreation
    startDate = models.DateField()
    endDate = models.DateField()
    finishedDate = models.DateField()
    isCompleted = models.BooleanField(default=False)
    isPrinted = models.BooleanField(default=False)
    priority = models.CharField(max_length=10,blank=True,null=True)  # low,medium,high selection
    jobType = models.CharField(max_length=100,blank=True,null=True) #short description about the job.
    tradesNumber = models.CharField(max_length=10,blank=True,null=True)
    
    # #Costs, Estimated.
    # labourCost = models.CharField(max_length=100,blank=True,null=True)
    # materialCost = models.CharField(max_length=100,blank=True,null=True)
    # otherCost = models.CharField(max_length=100,blank=True,null=True)
    # total = models.CharField(max_length=100,blank=True,null=True)
    
    # #Costs, Actual.
    # labourCost = models.CharField(max_length=100,blank=True,null=True)
    # materialCost = models.CharField(max_length=100,blank=True,null=True)
    # otherCost = models.CharField(max_length=100,blank=True,null=True)
    # total = models.CharField(max_length=100,blank=True,null=True)
    
    #spares..
    spareName = models.CharField(max_length=100,blank=True,null=True)  #It should be the foreign key for just borrow proc-
    unit = models.IntegerField()
    
    #trades....
    tradesList = models.CharField(max_length=100,blank=True,null=True)  #list ya watakaofanya kazi angalia hapo kak.
    isTradesConfirmed = models.BooleanField(default=False)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_maintenanceschedule",blank=True,null=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_maintenanceschedul",blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.serialNumber)
    

