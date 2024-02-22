from rest_framework import serializers
from main.models import Xodimlar




class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Xodimlar
        fields='__all__'



class XodimlarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Xodimlar
        fields='__all__'