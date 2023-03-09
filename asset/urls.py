from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetManageView, name='AssetManage_url'),
    
    #system settings urls path.
    path('department/', views.DepartmentView, name='department_url'),
    path('createDepartment/', views.CreateDepartmentView, name='createDepartment_url'),
    path('departmentStatus/', views.DepartmentStatusView, name="departmentStatus_url"),
    path('deleteDepartment/<str:pk>', views.DeleteDepartmentView, name='deleteDepartment_url'),
    
    path('categoryList/', views.CategoryListView, name='categoryList_url'),
    path('createCategoryOne/', views.CreateCategoryOneView, name='createCategoryOne_url'),
    path('statusCategoryOne/', views.StatusCategoryOneView, name='statusCategoryOne_url'),
    path('deleteCategoryOne/<str:pk>', views.DeleteCategoryOneView, name='deleteCategoryOne_url'),
    path('createCategoryTwo/', views.CreateCategoryTwoView, name='createCategoryTwo_url'),
    path('statusCategoryTwo/', views.StatusCategoryTwoView, name='statusCategoryTwo_url'),
    path('deleteCategoryTwo/<str:pk>', views.DeleteCategoryTwoView, name='deleteCategoryTwo_url'),
    path('createTradesSetting/', views.CreateTradesSettingView, name='createTradesSetting_url'),
    path('updateTradesSetting/<str:pk>', views.UpdateTradesSettingView, name='updateTradesSetting_url'),
    
    path('stationOfficeList/', views.StationOfficeListView, name='stationOfficeList_url'),
    path('createStation/', views.CreateStationView, name='createStation_url'),
    path('stationStatus/', views.StationStatusView, name='stationStatus_url'),
    path('updateStation/<str:pk>', views.UpdateStationView, name='updateStation_url'),
    path('createOffice/', views.CreateOfficeView, name="createOffice_url"),
    path('officeStatus/', views.OfficeStatusView, name='officeStatus_url'),
    path('updateOffice/<str:pk>', views.UpdateOfficeView, name='updateOffice_url'),
]