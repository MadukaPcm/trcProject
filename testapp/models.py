from django.db import models
import uuid
from datetime import date,timedelta
from uaa.models import User

# PREVENTIVE MAINTENANCE MODELS............
class LocomotiveType(models.Model): #(Are two MAin line and shutting L)
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    typeL = models.CharField(max_length=100,blank=True,null=True)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    # @property
    # def IsDueForM(self):
    #     return (date.today()-self.lastMaintained).days >= (self.mtl-3)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.typeL)
    
class LocomotiveClass(models.Model): #(They are bout 7 classes.)
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    className = models.CharField(max_length=100,blank=True,null=True)
    locomotive_type = models.ForeignKey(LocomotiveType, related_name='locomotiveL_type', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.className)
    
class ServiceType(models.Model): #(They are 3 electrical, mech and mixer.)
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    
    
    
    def __str__(self):
        return str(self.name)
    
class ClassService(models.Model): #(They are 3 electrical, mech and mixer.)
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    service_type = models.ForeignKey(ServiceType, related_name='servicec_type', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    class_type = models.ForeignKey(LocomotiveClass, related_name='classs_type', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    serviceName = models.CharField(max_length=100,blank=True,null=True)
    time_schedule = models.IntegerField(default=0) # time schedule in days
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.serviceName)
    
class ServiceSheet(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    service_class = models.ForeignKey(ClassService, related_name='servicecS_class', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=100,blank=True,null=True)
    taskDescription = models.TextField()
    timeSTD = models.CharField(max_length=100,blank=True,null=True)
    grade = models.CharField(max_length=20,blank=True,null=False)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    

class Locomotive(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    classL = models.ForeignKey(LocomotiveClass, related_name='locom_class', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    locomotiveNumber = models.CharField(max_length=100,blank=True,null=True)
    maintenanceNumber = models.IntegerField(default=0)
    isTobescheduled = models.BooleanField(default=True)
    goingRootNo = models.IntegerField(default=0)
    returningRootNo = models.IntegerField(default=0)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.locomotiveNumber)
    

class Workshop(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    workshopName = models.CharField(max_length=100,blank=True,null=True)
    region = models.CharField(max_length=50,blank=True,null=True)
    district = models.CharField(max_length=50,blank=True,null=True)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.workshopName)
    
#Preventive maintenance schedule report.........
class LocomotiveMaintenance(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    reportUniqueCode = models.CharField(max_length=100,null=True,blank=True,unique=True)
    locomotive = models.ForeignKey(Locomotive, related_name='locomotive_report', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    classService = models.ForeignKey(ClassService, related_name='classService_report', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.ForeignKey(Workshop, related_name='WorkshopRreport', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    ex_maintenace_date = models.DateField()
    actual_maintenance_date = models.DateField()
    isConfirmed = models.BooleanField(default=False)
    confirmedBy = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_deputy',null=True,blank=True)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.reportUniqueCode)
    
class ServiceSheetReport(models.Model): #send email notification engineer for specific workshop. getting list of deputies
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    reportUniqueCode = models.CharField(max_length=100,null=True,blank=True)
    serviceSheet = models.ForeignKey(ServiceSheet, related_name='servicesReport', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    isChecked = models.BooleanField(default=False)
    description = models.TextField()
    checkedBy = models.ForeignKey(User, related_name='user_checker',on_delete=models.CASCADE,null=True,blank=True) #request.user
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.id)    
    

#BREAK DOWN MAINTENANCE MODEL PART ......
class ReportFault(models.Model): #send email notification engineer for specific workshop. getting list of deputies
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    workshop = models.ForeignKey(Workshop, related_name='WorkshopRpt', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    fault = models.CharField(max_length=50,blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    faultDate = models.DateField()
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.fault)
    
class BreakDownM(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    locomotive = models.ForeignKey(Locomotive, related_name='locom', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.ForeignKey(Workshop, related_name='WorkshopBd', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    fault = models.CharField(max_length=50,blank=True,null=True)
    description = models.CharField(max_length=255,blank=True,null=True)
    faultDate = models.DateField()
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.fault)


#AVAILABILITY AND RELIABILITY MODEL PART....
class RootType(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    rootName = models.CharField(max_length=100,blank=True,null=True)  # is going and is returning
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.rootName)
    
class PassLocomotive(models.Model):
    id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True,primary_key=True)
    locomotive = models.ForeignKey(Locomotive, related_name='locomotiveA', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    workshop = models.ForeignKey(Workshop, related_name='WorkshopA', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    root = models.ForeignKey(RootType, related_name='rootT', 
                                   on_delete=models.CASCADE, null=True, blank=True)
    rootDate = models.DateTimeField()
    arrivalStatus = models.CharField(max_length=200,blank=True,null=False) #safe or with fault...
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status= models.BooleanField(default=True)
    
    class Meta:
        ordering =['-createdAt','-updatedAt']
    
    def __str__(self):
        return str(self.locomotive.locomotiveNumber)
    
