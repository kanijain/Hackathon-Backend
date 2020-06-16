from django.shortcuts import render
from food.models import (
    Food,
    FoodNutrition,
)
from rest_framework import filters
from rest_framework import status

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from info.models import(
    Profile
)
from info.api.v0.serializers import(
    DailyDietReadSserializer

)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodSerializer,FoodReadSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class AllFoodViews(generics.ListCreateAPIView):
    queryset=FoodNutrition.objects.all()
    serializer_class = FoodReadSerializer
    search_fields = ['name']
    http_method_names = ['get']

    filter_backends = (filters.SearchFilter,)
    def list(self,request,*args,**kwargs):
        self.object_list=self.filter_queryset(self.get_queryset())
        serializer=self.get_serializer(self.object_list,many=True,context={'request': request})
        context={}
        data={}
        obj=serializer.data[0]
        data=obj
        return Response(data)



@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def get_food(request):
    context={}
    data={}
    context['sucess']=True
    context['status']=200
    context['response']="sucessfull"
    try:
            obj=get_object_or_404(Profile,User=request.user)
    except:
        context['sucess']=False
        context['status']=400
        context['data']=data
        context['message']="profile dosen't exist"
        return Response(context)
    
    qs=FoodNutrition.objects.filter(name="Bell Peppers")
    # qs=qs| Food.objects.filter(name="poha")
    # qs=qs| Food.objects.filter(name="Apples")
    # qs=qs| Food.objects.filter(name="Chicken Boiled")
    # qs=qs| Food.objects.filter(name="Sushi Topped With Salmon")
    # qs=qs| Food.objects.filter(name="Brown Rice")
    # qs=qs| Food.objects.filter(name="Pie Tofu With Fruit")
    # qs=qs| Food.objects.filter(name="Hard Boiled Eggs")
    # qs=qs| Food.objects.filter(name="Mushrooms")
    context['count']=qs.count()
    serializer_class = FoodSerializer(qs,many=True,context={'request': request})
    data=serializer_class.data
    context['data']=data
    return Response(data)

