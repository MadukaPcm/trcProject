from django.shortcuts import render
from django.utils import timezone
from datetime import date,timedelta
import random
import string
from . models import *

# Create your views here.
def TestView(request):
    
    charaters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(charaters) for i in range(10))
    now = timezone.now()
    print(now)
    
    lc = Locomotive.objects.filter(isTobescheduled=True)
    for locomotive in lc:
        lcinstance = locomotive.classL
        for service in ClassService.objects.filter(status=True,class_type=lcinstance):
            isAvailable = LocomotiveMaintenance.objects.filter(locomotive=locomotive,classService=service).first()
            try:
                last_maintained = LocomotiveMaintenance.objects.filter(locomotive=locomotive,classService=service).latest('actual_maintenance_date')
            except LocomotiveMaintenance.DoesNotExist:
                last_maintained = None
            if isAvailable:
                timeDiff = (date.today()-last_maintained.actual_maintenance_date).days >= (service.time_schedule)
                if timeDiff:
                    print("maintenance is needed")
                print("Available")
                print(last_maintained.actual_maintenance_date)
            else:
                print(str(locomotive)+" "+ service.serviceName)
    # lclass = lc.c
    # for cs in ClassService.objects.filter(class_type_id=lclass):
    #     cs_data = cs

    # @property
    # def IsDueForM(self):
    #     return (date.today()-self.lastMaintained).days >= (self.mtl-3)
    
    print(last_maintained)
    # print(service)
    # print(cs_data)
    
    context = {}
    return render(request, 'test/test.html', context)

def TestsView(request):
    
    context = {}
    return render(request, 'test/tests.html', context)
