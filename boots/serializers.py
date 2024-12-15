import io
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Boots



# class BootsModel:
#     def __init__(self, title, description,):
#         self.title = title
#         self.description = description
    

class BootsSerializer(serializers.Serializer):
    title = serializers.CharField( max_length=100)
    description = serializers.CharField()
    category_id = serializers.IntegerField()
    price = serializers.IntegerField()
    image = serializers.ImageField()
    
    
    def create(self, validated_data):
        return Boots.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.price = validated_data.get("price", instance.price)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance
    
    
# def encode():
#     model = BootsModel('adidas', 'description: adidas')
#     model_sr = BootsSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
    
    
# def decode():
#     stream = io.BytesIO(b'{"title":"adidas","description":"description: adidas"}')
#     data = JSONParser().parse(stream)
#     serializer = BootsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)