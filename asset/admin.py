from django.contrib import admin 
from . models import Station,Office,CategoryTwo,SpareTool,Asset

# Register your models here.
admin.site.register(Station)
admin.site.register(Office)
admin.site.register(CategoryTwo)
admin.site.register(SpareTool)
admin.site.register(Asset)

