from django.db import models
from uaa.models import User
from uaa.models import Department
from django.core.validators import FileExtensionValidator
import uuid

# Create your models here. 
class Station(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_station', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    stationName = models.CharField(max_length=100,blank=True,null=True)
    stationNumber = models.CharField(max_length=100,blank=True,null=True)
    regionName = models.CharField(max_length=100,blank=True,null=True)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_stations")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_station")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.stationName)
    
class Office(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_office', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    station = models.ForeignKey(Station, related_name='station_office',on_delete=models.DO_NOTHING)
    
    officeName = models.CharField(max_length=100,blank=True,null=True)
    OfficeNumber = models.CharField(max_length=100,blank=True,null=True)
    yearBuilt = models.DateField()
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_office")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_offce")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.officeName)
    
    
class CategoryTwo(models.Model): #[ air conditioner, plumbing, tv-dstv ]
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_categoryTwo', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_categoryTwo")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_categryTwo")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.name)   
    
class SpareTool(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_spareTool', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    spareSerialNo = models.CharField(max_length=100,blank=True,null=True)
    spareName = models.CharField(max_length=100,blank=True,null=True)
    unit = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_spareTools")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_spareTool")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.spareName)
    
    
class Asset(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    department = models.ForeignKey(Department, related_name='department_asset', 
                                   on_delete=models.DO_NOTHING, null=True, blank=True)
    office = models.ForeignKey(Office, related_name='office_asset',on_delete=models.DO_NOTHING)
    categoryTwo = models.ForeignKey(CategoryTwo, related_name='CategoryTwo_assets',on_delete=models.DO_NOTHING)
    spareTool = models.ForeignKey(SpareTool, related_name = 'SpareTool_asset', on_delete=models.DO_NOTHING)
    serialNumber = models.CharField(max_length=100,blank=True,null=True)
    assetName = models.CharField(max_length=100,blank=True,null=True)           
    # costSpent = models.CharField(max_length=100,blank=True,null=True)
    totalPrice = models.CharField(max_length=100,blank=True,null=True)
    lifeSpan = models.CharField(max_length=100,blank=True,null=True)
    mtl = models.CharField(max_length=100,blank=True,null=True)  #maintenance time length.
    siteName = models.CharField(max_length=100,blank=True,null=True) #place placed. eng....Trc-posta.
    # userManual = models.FileField(upload_to='userManual/asset/', 
    #                                 validators=[FileExtensionValidator(
    #                                     allowed_extensions=['pdf','docx','ppt'])],
    #                                 null=True,blank=True)
    orderStatus = models.BooleanField(default=True)
    vendor = models.CharField(max_length=100,blank=True,null=True)
    # description = models.TextField()
    iam = models.BooleanField(default=True) #is automatic schedule manteined
    maintenanceNumber = models.IntegerField(default=0)
    unit = models.IntegerField(default=0)
    lastMaintained = models.DateField(null=True, blank=True)

    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_assets")
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_asset")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.serialNumber)