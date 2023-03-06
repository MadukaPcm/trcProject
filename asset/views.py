from django.shortcuts import render,HttpResponse

# Create your views here.
def AssetManageView(request):
    
    context = {}
    return render(request, '', context)

# system settings function views.
def CategoryListView(request):
    
    context = {}
    return render(request, 'settings/categoryList.html', context)

def StationOfficeListView(request):
    
    context = {}
    return render(request, 'settings/stationOffice.html', context)