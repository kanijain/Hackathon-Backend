from rest_framework import serializers
from food.models import(
    Food,
    FoodNutrition,
    Problem,
    AvailablityZone
)

class FoodSerializer(serializers.ModelSerializer):
    #photo_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)


    class Meta():
        model = FoodNutrition
        fields = ['name','Calories','Fat','Protein','Carbohydrate','Image','id']
    def get_photo_url():
        request = self.context.get('request')
        photo_url = Food.Image.url
        return request.build_absolute_uri(photo_url)
        
class ProblemSerializer(serializers.ModelSerializer):
    class Meta():
        model=Problem
        fields= ['name']

class AvailablitySerializer(serializers.ModelSerializer):
    class Meta():
        model=AvailablityZone
        fields= ['name']


class FoodReadSerializer(serializers.ModelSerializer):
    Food_Group=serializers.SerializerMethodField('get_food_group')
    Category=serializers.SerializerMethodField('get_category')
    AvailablityTier=serializers.SerializerMethodField('get_availablity')
    Processing_level=serializers.SerializerMethodField('get_Processing_level')
    Problems_Can_Solve=ProblemSerializer(many=True,
        read_only=True
    )
    Availablity=AvailablitySerializer(many=True,
        read_only=True
    )
    Vitamin=serializers.SerializerMethodField('get_Vitamin')
    class Meta():
        model = FoodNutrition
        fields = ['name','description','Food_Group','Unitconversion','Calories','Lactose_Intolerance','Fat','Protein','Carbohydrate','Vitamin','Sugars','Fiber','Cholesterol','Saturated_Fats','Image','Availablity','Problems_Can_Solve','Processing_level','AvailablityTier','Category','Food_Group','id']
    def get_food_group(self,info):
        data=info.Food_Group.name
        return data
    def get_category(self,info):
        data=info.Category.name
        return data
    def get_availablity(self,info):
        data=info.AvailablityTier.name
        return data

    def get_Vitamin(self,info):
        data=info.Vitamin.name
        return data
    def get_Processing_level(self,info):
        data=info.Processing_level.Level
        return data
