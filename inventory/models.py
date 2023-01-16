from django.db import models
from uaa.models import User,Branch
from django.core.validators import FileExtensionValidator
import uuid

class Category(models.Model): #eg- office,electric station,rolling stock,spare part, recommended [spare pard and assets]
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    branch = models.ForeignKey(Branch, related_name='branch_category',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=255,blank=True,null=True)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_category",blank=True,null=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_categry",blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.name)
    
class OfficeStation(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    branch = models.ForeignKey(Branch, related_name='branch_officeStation',on_delete=models.DO_NOTHING)
    
    officeName = models.CharField(max_length=100,blank=True,null=True)
    OfficeNumber = models.CharField(max_length=100,blank=True,null=True)
    regionName = models.CharField(max_length=100,blank=True,null=True)
    yearBuilt = models.DateField()
    isStandard = models.BooleanField(default=False)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_office",blank=True,null=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_offce",blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.officeName)
    
    
class Inventory(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    branch = models.ForeignKey(Branch, related_name='branch_inventory',on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, related_name='category_inventry',on_delete=models.DO_NOTHING)
    
    serialNumber = models.CharField(max_length=100,blank=True,null=True)
    assetName = models.CharField(max_length=100,blank=True,null=True)
    costSpent = models.CharField(max_length=100,blank=True,null=True)
    totalPrice = models.CharField(max_length=100,blank=True,null=True)
    lifeSpan = models.CharField(max_length=100,blank=True,null=True)
    mtl = models.CharField(max_length=100,blank=True,null=True)  #maintenance time length.
    siteName = models.CharField(max_length=100,blank=True,null=True) #place placed. eng....Trc-posta.
    userManual = models.FileField(upload_to='userManual/', 
                                    validators=[FileExtensionValidator(
                                        allowed_extensions=['pdf','docx','ppt'])],
                                    null=True,blank=True)
    orderStatus = models.BooleanField(default=False)
    vendor = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField()
    iam = models.BooleanField(default=False) #is automatic schedule manteined
    maintenanceNumber = models.IntegerField(default=0)
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_inventory",blank=True,null=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_inventry",blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.serialNumber)



class TradesSetting(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    branch = models.ForeignKey(Branch, related_name='branch_tradesSettings',on_delete=models.DO_NOTHING)
    maxTradeNumber = models.IntegerField()
    
    createdBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_tradesSetting",blank=True,null=True)
    updatedBy = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="user_tradesSettings",blank=True,null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.maxTradeNumber)
    