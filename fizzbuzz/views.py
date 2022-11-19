from django.http import JsonResponse
from .models import Fizzbuzz
from .serializers import FizzbuzzSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def fizzbuzz_list(request):

    if request.method == 'GET':
        fizzbuzz = Fizzbuzz.objects.all()
        serializer = FizzbuzzSerializer(fizzbuzz, many=True) 
        return JsonResponse({'fizzbuzz': serializer.data})

    if request.method == 'POST':
        serializer = FizzbuzzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
