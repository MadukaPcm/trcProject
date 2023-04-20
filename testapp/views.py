from django.shortcuts import render
import random
import string
from . models import *

# Create your views here.
def TestView(request):
    
    charaters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(charaters) for i in range(10))
    
    lc = Locomotive.objects.filter(isTobescheduled=True)
    for locomotive in lc:
        lcinstance = locomotive.classL
        for service in ClassService.objects.filter(status=True,class_type=lcinstance):
            isAvailable = LocomotiveMaintenance.objects.filter(locomotive=locomotive,classService=service).first()
            if isAvailable:
                print("Available")
            else:
                print(str(locomotive)+" "+ service.serviceName)
    # lclass = lc.c
    # for cs in ClassService.objects.filter(class_type_id=lclass):
    #     cs_data = cs
    
    print(locomotive)
    # print(service)
    # print(cs_data)
    
    context = {}
    return render(request, 'test/test.html', context)

def TestsView(request):
    
    context = {}
    return render(request, 'test/tests.html', context)
