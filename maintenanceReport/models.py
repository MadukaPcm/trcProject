from django.db import models
from uaa.models import User,Branch 
from workOrder.models import MaintenanceSchedule
from django.core.validators import FileExtensionValidator
import uuid


class MaintenanceReport(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    branch = models.ForeignKey(Branch, related_name='branch_maintenanceSchedule',on_delete=models.DO_NOTHING)
    jobDescription = models.TextField()
    completionDate = models.DateField()
    isCompleted = models.BooleanField(default=False)
    other = models.CharField(max_length=100,null=True,blank=False)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_maintenanceReport",blank=True,null=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_maintenanceReprt",blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):    #the report is only created when order was confirmed.
        return str(self.maxTradeNumber)
