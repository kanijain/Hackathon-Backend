from django.db import models

# Create your models here.
class Food(models.Model):
    PID=models.PositiveIntegerField(null=True)
    name=models.CharField(max_length=255)
    Food_Group=models.CharField(max_length=255,null=True)
    Calories=models.PositiveIntegerField(null=True)
    Fat=models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Protein =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Carbohydrate =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Sugars =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Fiber =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Cholesterol =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Saturated_Fats =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Image=models.ImageField(upload_to='Food/',null=True,blank=True)
    def __str__(self):
        return self.name

class FoodGroup(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
            return self.name
    

class Category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
            return self.name

class AvailablityLevel(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
            return self.name

class Processing(models.Model):
    Level=models.CharField(max_length=255)
    def __str__(self):
            return self.Level


class Problem(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
            return self.name

class AvailablityZone(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
            return self.name

class Vitamins(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
            return self.name

class FoodNutrition(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    Food_Group = models.ForeignKey(FoodGroup, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    AvailablityTier = models.ForeignKey(AvailablityLevel, on_delete=models.CASCADE)
    Processing_level=models.ForeignKey(Processing,on_delete=models.CASCADE)
    Unitconversion=models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=4)
    Calories=models.PositiveIntegerField(null=True)
    Lactose_Intolerance=models.BooleanField(default=False)
    Fat=models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Protein =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Carbohydrate =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Vitamin=models.ForeignKey(Vitamins,on_delete= models.CASCADE)
    Sugars =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Fiber =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Cholesterol =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Saturated_Fats =models.DecimalField(decimal_places=2, null=True, blank=True,max_digits=10)
    Image=models.ImageField(upload_to='Foodx/',null=True,blank=True)
    Problems_Can_Solve=models.ManyToManyField(Problem)
    Availablity=models.ManyToManyField(AvailablityZone)

    
    def __str__(self):
        return self.name