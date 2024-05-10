from django.contrib import admin
from testapp.models import *

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','eligibility','address','email','phonenumber']

admin.site.register(HydJobs, HydjobsAdmin)

class BngjobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','eligibility','address','email','phonenumber']

admin.site.register(BngJobs, BngjobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display = ['id','date','company','title','eligibility','address','email','phonenumber']

admin.site.register(PuneJobs, PunejobsAdmin)