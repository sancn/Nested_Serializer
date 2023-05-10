from .models import *
from rest_framework import serializers

class DefaulModelSerializer(serializers.ModelSerializer):
  @property
  def request(self):
    return self.context['request']
  
  def validate(self, attrs):
    #  user = self.context.user
    user = self.request.user


    #  import ipdb;ipdb.set_trace()    
    print("the user is:-----------------------------------", user)
    return super().validate(attrs)
   

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields= '__all__'

    # def validate(self, attrs):
    #   if self.request.user.is_authenticated:
    #     user = self.request.user
    #     print("*****************---->", user)  
    #   else:
    #     print("No user authenticated")
    #   return super().validate(attrs)




class SingerSerializer(DefaulModelSerializer):
  sungby=SongSerializer(many=True,read_only=True)
  class Meta:
    model=Singer
    fields= '__all__'

# yo kura lai mathi default serializer banyera overwrite gareko xa
  # def validate(self, attrs):
  #   user = self.context['request'].user

  #   import ipdb;ipdb.set_trace()    
  #   print("the user is:-----------------------------------", user)
    
  #   return attrs
  # @property
  # def request(self):
  #   return self.context['request']@property
  # def request(self):
  #   return self.context['request']
  
  # def validate(self, attrs):
  #   #  user = self.context.user
  #   user = self.request.user


  #   #  import ipdb;ipdb.set_trace()    
  #   print("the user is:-----------------------------------", user)
  #   return super().validate(attrs)
  
  
  # def validate(self, attrs):
  #   #  user = self.context.user
  #   user = self.request.user


  #   #  import ipdb;ipdb.set_trace()    
  #   print("the user is:-----------------------------------", user)
  #   return super().validate(attrs)
  
  

