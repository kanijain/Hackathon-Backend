from rest_framework import serializers
from info.models import (Profile,
DailyDiet,
MedicalForm,
)
from food.models import(
    Problem
)
from food.api.v0.serializers import(
    FoodSerializer
)
class ProfileSerializer(serializers.ModelSerializer):

    class Meta():
        model = Profile
        fields = ['gender', 'name','weight', 'height', 'goals', 'activity','age','lactoseIntolerance','foodChoice']

class ProfileReadSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField('get_username')
    condition=serializers.SerializerMethodField('get_Condition')
    gender=serializers.SerializerMethodField('get_Gender')
    activity=serializers.SerializerMethodField('get_Activity')
    goals=serializers.SerializerMethodField('get_Goals')
    foodChoice=serializers.SerializerMethodField('get_choice')

    class Meta():
        model = Profile
        fields = ['gender', 'name','weight', 'height', 'goals', 'activity','age','username','bmi','dailyCalories','bmr','condition','foodChoice','lactoseIntolerance']

    def get_username(self,info):
        data=info.User.username
        return data
    def get_Condition(self,info):
        data=info.condition
        if data=='1':
            return "Underweight"
        if data=='2':
            return "Normal"
        if data=='3':
            return "Overweight"
        if data=='4':
            return "Obesity"
    def get_Gender(self,info):
        data=info.gender
        a=''
        if data=='1':
            a= "Male"
        if data=='2':
            a= "Female"
        return a
    def get_Goals(self,info):
        data=info.goals
        a=''
        if data=='1':
            a= "Extreme Loose Weight"
        if data=='2':
            a= "Minor Loose Weight"
        if data=='3':
            a= "Maintain Weight"
        if data=='4':
            a= "Weight gain"        
        if data=='5':
            a= "Extreme Weight gain"
        return a
    def get_Activity(self,info):
        data=info.activity
        if data=='1':
            return "Sedentary"
        if data=='2':
            return "Lightly Active"
        if data=='3':
            return "Active"
        if data=='4':
            return "Very Active"
    def get_choice(sel,info):
        data=info.foodChoice.name
        return data

class DailyDietSserializer(serializers.ModelSerializer):
    class Meta:
        model=DailyDiet
        fields=['mark','comment','item','amount']



class DailyDietReadSserializer(serializers.ModelSerializer):
    itemname=serializers.SerializerMethodField('get_item')
    calories=serializers.SerializerMethodField('get_calories')
    image=serializers.SerializerMethodField('get_image')
    class Meta:
        model=DailyDiet
        fields=['mark','comment','amount','id','itemname','image','calories']
    def get_item(self,info):
        data=info.item.name
        return data
    def get_calories(self,info):
        data=info.item.Calories
        return data
    def get_image(self,info):
        data=info.item.Image
    


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Problem
        fields='__all__'

class MedicalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicalForm
        fields=('bloodGroup','problem','description')

class MedicalFormReadSerializer(serializers.ModelSerializer):   
    bloodGroup=serializers.SerializerMethodField('get_bloodGroup')
    problem=ProblemSerializer(many=True,
        read_only=True
    )
    class Meta:
        model=MedicalForm
        fields=('bloodGroup','description','problem')
    def get_bloodGroup(self,info):
        data=info.bloodGroup.name
        return data