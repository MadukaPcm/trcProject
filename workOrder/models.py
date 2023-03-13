from django.db import models
from uaa.models import User
from inventory.models import Inventory
from asset.models import SpareTool,Asset
from uaa.models import Department
from django.core.validators import FileExtensionValidator
import uuid
import datetime

class MaintenanceSchedule(models.Model):  #this is maintenance order
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_maintenanceSchedule', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    inventory = models.ForeignKey(Inventory, related_name='inventory_maintenanceSchedule',
                                  on_delete=models.DO_NOTHING, blank=True, null=True)
    asset = models.ForeignKey(Asset, related_name='asset_maintenanceSchedule',
                              on_delete=models.DO_NOTHING, blank=True,null=True)
    OrderNumber = models.CharField(max_length=100,blank=True,null=True) #THis should automatic be filled.
    
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
    
    #spares..
    spareTool = models.ForeignKey(SpareTool, related_name = 'SpareTool_MaintenanceSchedule', on_delete=models.DO_NOTHING)
    unit = models.IntegerField()
    
    #trades....
    tradesList = models.ManyToManyField(User, related_name = 'userList_maintenanceSchedule')  #list ya watakaofanya kazi angalia hapo kak.
    isTradesConfirmed = models.BooleanField(default=False)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_maintenanceschedule")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_maintenanceschedul")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.OrderNumber)
    
    # @property
    # def noDays(self):
    #     return ((datetime.date.today()) - self.issueDate).days
    

