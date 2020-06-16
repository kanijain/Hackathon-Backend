from django.contrib import admin
from info.models import (
    Profile,
    BloodGroup,
    MedicalForm,
    DailyDiet

)
# Register your models here.
admin.site.register(Profile)

admin.site.register(DailyDiet)
admin.site.register(BloodGroup)
admin.site.register(MedicalForm)
