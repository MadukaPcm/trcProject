from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from asset.models import Station,Office,CategoryTwo,SpareTool,Asset
from inventory.models import CategoryOne,TradesSetting
from uaa.models import Department
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def SpareToolView(request):
    departmentInstance = Department.objects.all()
    spareToolInstance = SpareTool.objects.all()
    
    context = {'departmentInstance':departmentInstance, 'spareToolInstanceData':spareToolInstance}
    return render(request, 'assets/spareTool.html', context)

def CreateSpareToolView(request):
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            SpareSerialNo = request.POST.get('SpareSerialNo')
            SpareName = request.POST.get('SpareName')
            Unit = request.POST.get('Unit')
            
            createspInstance = SpareTool.objects.create(
                department_id=DepartmentId,
                spareSerialNo=SpareSerialNo,
                spareName=SpareName,
                unit=Unit,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id
            )
            createspInstance.save()
            messages.success(request, 'spare-tool created successfully')
            return redirect('spareTool_url')
        
    except:
        return render(None, 'uaa/error500.html')

def SpareToolStatusView(request):
    try:
        spStatusInstance = get_object_or_404(SpareTool,pk=request.GET.get('spStatus_id'))
        spStatusInstance.status = not spStatusInstance.status
        spStatusInstance.save()
        messages.info(request, 'status successfully changed')
        return redirect('spareTool_url')

    except:
        return render(None, 'uaa/error500.html')

def UpdateSpareToolView(request, pk):
    try:
        updatespInstance = SpareTool.objects.filter(id=pk)
        
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            SpareSerialNo = request.POST.get('SpareSerialNo')
            SpareName = request.POST.get('SpareName')
            Unit = request.POST.get('Unit')
            
            SpareTool.objects.filter(id=pk).update(
                department_id=DepartmentId,
                spareSerialNo=SpareSerialNo,
                spareName=SpareName,
                unit=Unit,
                updatedBy_id=request.user.id
            )
            messages.info(request, 'spare tools successfully updated')
            return redirect('spareTool_url')
    
    except:
        return render(None, 'uaa/error500.html')

def AssetManageView(request):
    dpi = Department.objects.all()
    ofci = Office.objects.all()
    ctti = CategoryTwo.objects.all()
    spti = SpareTool.objects.all()  
    
    assetInstance = Asset.objects.all()
    
    context = {"departmentObjectData":dpi, "officeInstanceData":ofci, "catTwoInstanceData":ctti, "spToolInstance":spti, "assetInstanceData":assetInstance}
    return render(request, 'assets/assetManage.html', context)

def CreateAssetView(request):
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            OfficeId = request.POST.get('OfficeId')
            catTwoId = request.POST.get('catTwoId')
            SpareId = request.POST.get('SpareId')
            SerialNo = request.POST.get('SerialNo')
            assetName = request.POST.get('assetName')
            SiteName = request.POST.get('SiteName')
            Vendor = request.POST.get('Vendor')
            TotalPrice = request.POST.get('TotalPrice')
            LifeSpan = request.POST.get('LifeSpan')
            Mtl = request.POST.get('Mtl')
            Lmd = request.POST.get('Lmd')
            Unit = request.POST.get('Unit')
            
            Asset.objects.create(
                department_id=DepartmentId,
                office_id=OfficeId,
                categoryTwo_id=catTwoId,
                spareTool_id=SpareId,
                serialNumber=SerialNo,
                assetName=assetName,
                totalPrice=TotalPrice,
                lifeSpan=LifeSpan,
                mtl=Mtl,
                siteName=SiteName,
                vendor=Vendor,
                unit=Unit,
                lastMaintained=Lmd,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'asset created successfully')
            return redirect('AssetManage_url')
    
    except:
        return render(None, 'uaa/error500.html')
    

def UpdateAssetView(request, pk):
    try:
        updateAssetInstance = Asset.objects.filter(id=pk)
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            OfficeId = request.POST.get('OfficeId')
            catTwoId = request.POST.get('catTwoId')
            SpareId = request.POST.get('SpareId')
            SerialNo = request.POST.get('SerialNo')
            assetName = request.POST.get('assetName')
            SiteName = request.POST.get('SiteName')
            Vendor = request.POST.get('Vendor')
            TotalPrice = request.POST.get('TotalPrice')
            LifeSpan = request.POST.get('LifeSpan')
            Mtl = request.POST.get('Mtl')
            Lmd = request.POST.get('Lmd')
            Unit = request.POST.get('Unit')
            
            Asset.objects.filter(id=pk).update(
                department_id=DepartmentId,
                office_id=OfficeId,
                categoryTwo_id=catTwoId,
                spareTool_id=SpareId,
                serialNumber=SerialNo,
                assetName=assetName,
                totalPrice=TotalPrice,
                lifeSpan=LifeSpan,
                mtl=Mtl,
                siteName=SiteName,
                vendor=Vendor,
                unit=Unit,
                lastMaintained=Lmd,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'asset updated successfully')
            return redirect('AssetManage_url')
    
    except:
        return render(None, 'uaa/error500.html')
    
def IsAutoMaintainedView(request):
    
    try:
        assetAutoInstance = get_object_or_404(Asset,pk=request.GET.get('isAuto_id'))
            
        assetAutoInstance.iam = not assetAutoInstance.iam
        assetAutoInstance.save()
        messages.info(request, 'auto maintainance status changed')
        return redirect('AssetManage_url')

    except:
        return render(None, 'uaa/error500.html')
    

def AssetStatusView(request):
    
    try:
        assetStatusInstance = get_object_or_404(Asset,pk=request.GET.get('assetStts_id'))
            
        assetStatusInstance.status = not assetStatusInstance.status
        assetStatusInstance.save()
        messages.info(request, 'status changed successfully')
        return redirect('AssetManage_url')

    except:
        return render(None, 'uaa/error500.html')
    

# system settings function views.  
def DepartmentView(request):
    try:
        departmentInstance = Department.objects.all()
    except:
        return render(None, 'uaa/error500.html')
    
    context = {"departmentInstance":departmentInstance}
    return render(request, 'settings/department.html', context)

def CreateDepartmentView(request):
    
    try:
        if request.method == "POST":
            Name = request.POST.get('Name')
            Email = request.POST.get('Email')
            PhoneNumber = request.POST.get('PhoneNumber')
            
            createDepartment = Department.objects.create(
                name=Name, 
                Email=Email, 
                phoneNumber=PhoneNumber,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id,
                )
            createDepartment.save()
            messages.success(request, 'department created successfully')
            return redirect('department_url')
            
            
    except:
        return render(None, 'uaa/error500.html')
        
def DepartmentStatusView(request):
    try:
        departmentStatus = get_object_or_404(Department,pk=request.GET.get('approveDepartment_id'))
        
        departmentStatus.status = not departmentStatus.status
        departmentStatus.save()
        messages.info(request, 'status successfully changed')
        return redirect('department_url')
    
    except:
        return render(None, 'uaa/error500.html')


def DeleteDepartmentView(request, pk):
    try:
        getDepartmentObject = Department.objects.get(id=pk)
        getDepartmentObject.delete()
        messages.error(request, 'department successfully deletedd !!!')
        return redirect('department_url')
    
    except:
        return render(None, 'uaa/error500.html')

def CategoryListView(request):
    try:
        CategoryTwoInstance = CategoryTwo.objects.all()
        totalCategoryTwo = CategoryTwo.objects.all().count()
        CategoryOneInstance = CategoryOne.objects.all()
        totalCategoryOne = CategoryOne.objects.all().count()
    
        tradesSettingInstance = TradesSetting.objects.all()
        departmentObjectData = Department.objects.all()
        
    except:
        return render(None, 'uaa/error500.html')
    
    context = {"CategoryTwoInstance":CategoryTwoInstance, "totalCategoryTwo":totalCategoryTwo, "CategoryOneInstance":CategoryOneInstance,"totalCategoryOne":totalCategoryOne, "tradesSettingInstance":tradesSettingInstance, "departmentObjectData":departmentObjectData}
    return render(request, 'settings/categoryList.html', context)

def CreateCategoryOneView(request):
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            categoryName = request.POST.get('categoryName')
            
            catOneInstance = CategoryOne.objects.create(
                department_id=DepartmentId,
                name=categoryName,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id,
            )
            catOneInstance.save()
            messages.success(request, 'cat..one successfully created')
            return redirect('categoryList_url')
            
    except:
        return render(None, 'uaa/error500.html')
        
def StatusCategoryOneView(request):
    try:
        categoryOneStatus = get_object_or_404(CategoryOne,pk=request.GET.get('catOne_id'))
        
        categoryOneStatus.status = not categoryOneStatus.status
        categoryOneStatus.save()
        messages.info(request, 'cat...one status changed')
        return redirect('categoryList_url')
    
    except:
        return render(None, 'uaa/error500.html')
        
def DeleteCategoryOneView(request, pk):
    
    try:
        getCategoryOneObject = CategoryOne.objects.get(id=pk)
        getCategoryOneObject.delete()
        messages.error(request, 'cat...one deleted successfully !!!')
        return redirect('categoryList_url')
    
    except:
        return render(None, 'uaa/error500.html')
        
        
def CreateCategoryTwoView(request):
    
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            categoryName = request.POST.get('categoryName')
            
            catTwoInstance = CategoryTwo.objects.create(
                department_id=DepartmentId,
                name=categoryName,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id,
            )
            catTwoInstance.save()
            messages.success(request, 'cat...two successfully created')
            return redirect('categoryList_url')
            
    except:
        return render(None, 'uaa/error500.html')
        
def StatusCategoryTwoView(request):
    try:
        categoryTwoStatus = get_object_or_404(CategoryTwo,pk=request.GET.get('catTwo_id'))
        
        categoryTwoStatus.status = not categoryTwoStatus.status
        categoryTwoStatus.save()
        messages.info(request, 'cat..two status changed')
        return redirect('categoryList_url')
    
    except:
        return render(None, 'uaa/error500.html')
        
def DeleteCategoryTwoView(request,pk):
    
    try:
        getcategoryTwoObject = CategoryTwo.objects.get(id=pk)
        getcategoryTwoObject.delete()
        messages.error(request, 'cat..two successfully deleted')
        return redirect('categoryList_url')
    
    except:
        return render(None, 'uaa/error500.html')
        
        
def CreateTradesSettingView(request):
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            maxNo = request.POST.get('maxNo')
            
            maxNoInstance = TradesSetting.objects.create(
                department_id=DepartmentId,
                maxTradeNumber=maxNo,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id,
            )
            maxNoInstance.save()
            messages.success(request, 'max....No successfully created')
            return redirect('categoryList_url')
            
    except:
        return render(None, 'uaa/error500.html')
        
def UpdateTradesSettingView(request,pk):
    try:
        maxNoInstanceU = TradesSetting.objects.filter(id=pk)
        if request.method == "POST":
            Department_idd = request.POST.get('DepartmentId')
            max_no = request.POST.get('maxNo')
            
            TradesSetting.objects.filter(id=pk).update(
                department_id=Department_idd,
                maxTradeNumber=max_no,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'max....No successfully updated')
            return redirect('categoryList_url')
        
    except:
        return render(None, 'uaa/error500.html')


def StationOfficeListView(request):
    try:
        stationInstance = Station.objects.all()
        totalStation = Station.objects.all().count()
        officeInstance = Office.objects.all()
        totalOffice = Office.objects.all().count()
        departmentObjectData = Department.objects.all()
        stationInstance = Station.objects.all()
    except:
        return render(None, 'uaa/error500.html')

    context = {"stationInstanceData":stationInstance, "totalStation":totalStation, "officeInstanceData":officeInstance, "totalOffice":totalOffice, "departmentObjectData":departmentObjectData, "stationInstanceData":stationInstance}
    return render(request, 'settings/stationOffice.html', context)

def CreateStationView(request):
    
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            StationName = request.POST.get('StationName')
            StationNumber = request.POST.get('StationNumber')
            REgionName = request.POST.get('REgionName')
            
            stationInstance = Station.objects.create(
                department_id=DepartmentId,
                stationName=StationName,
                stationNumber=StationNumber,
                regionName=REgionName,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id,
            )
            stationInstance.save()
            messages.success(request, 'station successfully created')
            return redirect('stationOfficeList_url')
            
    except:
        return render(None, 'uaa/error500.html')
        

def StationStatusView(request):
    try:
        stationStatusInstance = get_object_or_404(Station, pk=request.GET.get('station_id'))
        stationStatusInstance.status = not stationStatusInstance.status
        stationStatusInstance.save()
        messages.info(request, 'status successfully changed')
        return redirect('stationOfficeList_url')
    
    except:
        return render(None, 'uaa/error500.html')
        
def UpdateStationView(request, pk):
    updateStationInstance = Station.objects.filter(id=pk)
    
    try:
        if request.method == "POST":
            StationId = request.POST.get('StationId')
            DepartmentId = request.POST.get('DepartmentId')
            StationName = request.POST.get('StationName')
            StationNumber = request.POST.get('StationNumber')
            REgionName = request.POST.get('REgionName')
            
            Station.objects.filter(id=pk).update(
                department_id=DepartmentId,
                stationName=StationName,
                stationNumber=StationNumber,
                regionName=REgionName,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'station successfully updated')
            return HttpResponseRedirect('/asset/stationOfficeList')
        
    except:
        return render(None, 'uaa/error500.html')

def CreateOfficeView(request):
    
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            StationId = request.POST.get('StationId')
            OfficeName = request.POST.get('OfficeName')
            OfficeNumber = request.POST.get('OfficeNumber')
            YearBuilt = request.POST.get('YearBuilt')
            
            officeInstance = Office.objects.create(
                department_id=DepartmentId,
                station_id=StationId,
                officeName=OfficeName,
                OfficeNumber=OfficeNumber,
                yearBuilt=YearBuilt,
                createdBy_id=request.user.id,
                updatedBy_id=request.user.id,
            )
            officeInstance.save()
            messages.success(request, 'office successfully created')
            return redirect('stationOfficeList_url')
            
    except:
        return render(None, 'uaa/error500.html')
        
def OfficeStatusView(request):
    try:
        officeStatusInstance = get_object_or_404(Office, pk=request.GET.get('officeId'))
        officeStatusInstance.status = not officeStatusInstance.status
        officeStatusInstance.save()
        messages.info(request, 'status successfully changed')
        return HttpResponseRedirect('/asset/stationOfficeList')
    
    except:
        return render(None, 'uaa/error500.html')
        
        
def UpdateOfficeView(request, pk):
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            StationId = request.POST.get('StationId')
            OfficeName = request.POST.get('OfficeName')
            OfficeNumber = request.POST.get('OfficeNumber')
            YearBuilt = request.POST.get('YearBuilt')
            
            updateofficeInstance = Office.objects.filter(id=pk).update(
                department_id=DepartmentId,
                station_id=StationId,
                officeName=OfficeName,
                OfficeNumber=OfficeNumber,
                yearBuilt=YearBuilt,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'office row-date updated')
            return HttpResponseRedirect('/asset/stationOfficeList')
        
    except:
        return render(None, 'uaa/error500.html')
    