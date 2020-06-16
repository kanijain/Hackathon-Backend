from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from food.models import(
    FoodNutrition,
    Problem,
    Category
)

User = get_user_model()

CONDITION_CHOICES = (
    ('1','Underweight'),
    ('2', 'Normal'),
    ('3','Overweight'),
    ('4','Obesity'),
)
Goals_Choices=(
    (
        ('1','Extreme Loose Weight'),
        ('2','Minor Loose Weight'),
        ('3','Maintain Weight'),
        ('4','Weight gain'),
        ('5','Extreme Weight gain'),
    )
)
Activity_Choices=(
    (
        ('1','Sedentary'),
        ('2','Lightly Active'),
        ('3','Active'),
        ('4','Very Active'),

    )
)
Gender_CHOICES = (
    ('1','Male'),
    ('2', 'Female'),
    ('3','Transgender'),
)
class Profile(models.Model):
    User=models.OneToOneField(User , on_delete=models.CASCADE)
    name=models.CharField( max_length=255,)
    gender=models.CharField( max_length=1, choices=Gender_CHOICES)
    age=models.PositiveIntegerField()
    weight = models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(258)],)
    height =models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(210)],)
    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES)
    bmi=models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(35)],)
    goals=models.CharField(max_length=1, choices=Goals_Choices)
    activity=models.CharField(max_length=1, choices=Activity_Choices)
    dailyCalories=models.PositiveIntegerField()
    lactoseIntolerance=models.BooleanField()
    foodChoice=models.ForeignKey(Category,on_delete=models.CASCADE)
    bmr=models.FloatField(validators=[MinValueValidator(0.9), MaxValueValidator(10000)],)


# class DailyIntake(models.Model):
#     id=models.AutoField(primary_key=True,)
#     Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     Amount=models.DecimalField(decimal_places=1, null=True, blank=True,max_digits=10)
#     Item = models.ForeignKey(FoodNutrition, on_delete=models.CASCADE)
#     Mark=models.BooleanField()
#     comment=models.TextField()
#     def __str__(self):
#         return str(self.comment)

class DailyDiet(models.Model):
    mark=models.BooleanField(null=True)
    comment=models.TextField(null=True,blank=True)
    item = models.ForeignKey(FoodNutrition, on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True,)
    Timestamp=models.DateTimeField(auto_now_add=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=1,max_digits=10)



class BloodGroup(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name

class MedicalForm(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bloodGroup=models.ForeignKey(BloodGroup,on_delete=models.CASCADE)
    problem=models.ManyToManyField(Problem)
    description=models.TextField(blank=True,null=True)

    
