from django.http import JsonResponse
from .models import Fizzbuzz
from .serializers import FizzbuzzSerializer

def fizzbuzz_list(request):

    fizzbuzz = Fizzbuzz.objects.all()
    serializer = FizzbuzzSerializer(fizzbuzz, many=True) 
    return JsonResponse({"fizzbuzz": serializer.data}, safe=False)

