from rest_framework import serializers
from .models import Name

class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = "__all__"

    
