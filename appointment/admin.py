from django.contrib import admin

from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['a_doctor','a_patient','a_title','a_date','a_starttime','a_endtime']
    list_display_links = ('a_doctor','a_patient','a_title',)
    search_fields = ('a_doctor','a_patient','a_title',)
    list_filter = ('a_doctor','a_patient','a_title',)
    class Meta:
        model = Appointment
        def __str__(self):
            display =   self.a_doctor.fName + ' ' + self.a_doctor.lName + " has an appointment with " + self.a_patient.fName + ' ' + self.a_patient.lName + " at " + self.a_starttime.strftime('%I:%M %p') + " on " + self.a_date.strftime('%B %d, %Y')

            return display


admin.site.register(Appointment, AppointmentAdmin)
