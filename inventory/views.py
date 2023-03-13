from django.shortcuts import render,HttpResponse
from uaa.models import Department
from inventory.models import Inventory,CategoryOne
from asset.models import Office,SpareTool
from django.contrib import messages
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.http import HttpResponseRedirect

def InventoryView(request):
    dpi = Department.objects.all()
    ofci = Office.objects.all()
    ctti = CategoryOne.objects.all()
    spti = SpareTool.objects.all()  
    
    inventoryInstance = Inventory.objects.all()
    
    context = {"departmentObjectData":dpi,"catOneInstanceData":ctti, "spToolInstance":spti,"inventoryInstanceData":inventoryInstance}
    return render(request, 'inventory/manageInventory.html', context)

def CreateInventoryView(request):
    try:
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            catOneId = request.POST.get('catOneId')
            SpareId = request.POST.get('SpareId')
            SerialNo = request.POST.get('SerialNo')
            equipName = request.POST.get('equipName')
            SiteName = request.POST.get('SiteName')
            Vendor = request.POST.get('Vendor')
            TotalPrice = request.POST.get('TotalPrice')
            LifeSpan = request.POST.get('LifeSpan')
            Mtl = request.POST.get('Mtl')
            Lmd = request.POST.get('Lmd')
            Unit = request.POST.get('Unit')
            
            Inventory.objects.create(
                department_id=DepartmentId,
                categoryOne_id=catOneId,
                spareTool_id=SpareId,
                serialNumber=SerialNo,
                spareName=equipName,
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
            messages.success(request, 'Equipment created successfully')
            return redirect('Inventory_url')
        
    except:
        return render(None, 'uaa/error500.html')
    
    
def UpdateInventoryView(request, pk):
    try:
        inventoryInstance = Inventory.objects.filter(id=pk)
        if request.method == "POST":
            DepartmentId = request.POST.get('DepartmentId')
            catOneId = request.POST.get('catOneId')
            SpareId = request.POST.get('SpareId')
            SerialNo = request.POST.get('SerialNo')
            equipName = request.POST.get('equipName')
            SiteName = request.POST.get('SiteName')
            Vendor = request.POST.get('Vendor')
            TotalPrice = request.POST.get('TotalPrice')
            LifeSpan = request.POST.get('LifeSpan')
            Mtl = request.POST.get('Mtl')
            Lmd = request.POST.get('Lmd')
            Unit = request.POST.get('Unit')
            
            Inventory.objects.filter(id=pk).update(
                department_id=DepartmentId,
                categoryOne_id=catOneId,
                spareTool_id=SpareId,
                serialNumber=SerialNo,
                spareName=equipName,
                totalPrice=TotalPrice,
                lifeSpan=LifeSpan,
                mtl=Mtl,
                siteName=SiteName,
                vendor=Vendor,
                unit=Unit,
                lastMaintained=Lmd,
                updatedBy_id=request.user.id
            )
            messages.success(request, 'Equipment update successfully')
            return redirect('Inventory_url')
        
    except:
        return render(None, 'uaa/error500.html')
    
    
    
def IsAutoIMaintainedView(request):
    
    try:
        ivtryAutoInstance = get_object_or_404(Inventory,pk=request.GET.get('isAutoi_id'))
            
        ivtryAutoInstance.iam = not ivtryAutoInstance.iam
        ivtryAutoInstance.save()
        messages.info(request, 'auto maintainance status changed')
        return redirect('Inventory_url')

    except:
        return render(None, 'uaa/error500.html')
    
    
def InventoryStatusView(request):
    
    try:
        ivtryStatusInstance = get_object_or_404(Inventory,pk=request.GET.get('ivtry_id'))
            
        ivtryStatusInstance.status = not ivtryStatusInstance.status
        ivtryStatusInstance.save()
        messages.info(request, 'status changed successfully')
        return redirect('Inventory_url')

    except:
        return render(None, 'uaa/error500.html')