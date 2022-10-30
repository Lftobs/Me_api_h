from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Me(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'slackUsername' : 'Tobs',
            'backend' : bool(True),
            'age': 18,
            'bio' : 'im a very coolheaded person....i also love watching movies.'
            
        }
        return Response(data)
    