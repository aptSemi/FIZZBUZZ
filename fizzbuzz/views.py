from django.http import JsonResponse
from .models import Fizzbuzz
from .serializers import FizzbuzzSerializer

def fizzbuzz_list(request):

    #get all the fizzbuzz!
    #serialize the fizzy bubbly!
    #return json.....fizzy bubbly
    
    fizzbuzz = Fizzbuzz.objects.all()
    serializer = FizzbuzzSerializer(fizzbuzz, many=True) 
    return JsonResponse(serializer.data, safe=False)

