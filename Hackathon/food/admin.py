from django.contrib import admin
from food.models import (
    Food,
    FoodNutrition,
    Vitamins,
    AvailablityZone,
    Problem,
    Processing,
    AvailablityLevel,
    Category,
    FoodGroup
)
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Food)
class PersonAdmin(ImportExportModelAdmin):
    list_filter = ('Food_Group',)
    search_fields = ('name', )

    pass


@admin.register(FoodNutrition)
class PersonAdmin(ImportExportModelAdmin):
    list_filter = ('Vitamin','Availablity','Problems_Can_Solve','Processing_level' ,'AvailablityTier','Category',)
    search_fields = ('name', )
    pass


@admin.register(Vitamins)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(AvailablityZone)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Problem)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Processing)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(AvailablityLevel)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(FoodGroup)
class PersonAdmin(ImportExportModelAdmin):
    pass