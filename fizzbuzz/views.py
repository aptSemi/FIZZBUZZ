from django.http import JsonResponse
from .models import Fizzbuzz
from .serializers import FizzbuzzSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def fizzbuzz_list(request, format=None):

    if request.method == 'GET':
        fizzbuzz = Fizzbuzz.objects.all()
        serializer = FizzbuzzSerializer(fizzbuzz, many=True) 
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FizzbuzzSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def fizzbuzz_detail(request, id, format=None):

    try:
        fizzbuzz = Fizzbuzz.objects.get(pk=id)
    except Fizzbuzz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FizzbuzzSerializer(fizzbuzz)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FizzbuzzSerializer(fizzbuzz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fizzbuzz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
