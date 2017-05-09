from __future__ import absolute_import
from django.contrib import admin
from .models import Patient, Doctor, Nurse, Admin

class PatientAdmin(admin.ModelAdmin):
    list_display = ['fName','lName','gender','ePhone']
    list_display_links = ('fName','lName',)
    search_fields = ('fName','lName',)
    list_filter = ('gender','fName','lName',)
admin.site.register(Patient, PatientAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['fName','lName','hospital']
    list_display_links = ('fName','lName',)
    search_fields = ('fName','lName',)
    list_filter = ('hospital','fName','lName',)
    class Meta:
        model = Doctor
admin.site.register(Doctor, DoctorAdmin)

class NurseAdmin(admin.ModelAdmin):
    list_display = ['fName','lName','hospital']
    list_display_links = ('fName','lName',)
    search_fields = ('fName','lName',)
    list_filter = ('hospital','fName','lName',)
    class Meta:
        model = Nurse
admin.site.register(Nurse, NurseAdmin)

class AdminAdmin(admin.ModelAdmin):
    list_display = ['fName', 'lName', 'email']
    list_display_links = ('fName','lName',)
    search_fields = ('fName','lName',)
    list_filter = ('email','fName','lName',)
    class Meta:
        model = Admin
admin.site.register(Admin, AdminAdmin)
