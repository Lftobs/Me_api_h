from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import NameSerializers
from .models import Name


# Create your views here.
class Me(APIView):
    
    
    
    def get(self, request, *args, **kwargs):
        qs = Name.objects.all()
        serializer = NameSerializers(qs, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = NameSerializers(data=request.data)
        if serializer.is_valid():
            x = serializer.data['x']
            y = serializer.data['y']
            u = serializer.data['operation_type']
            if u == 'multiplication':
                f_res = x * y
            elif u == 'addition':
                f_res = x + y
            else:
                f_res = x - y
            final = {
                'slackUsername': 'Tobs',
                'result': f_res,
                'operation_type': u
            }
            return Response(final)
            #return Response(serializer.data)
        return Response(serializer.errors)
        
    