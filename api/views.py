from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# Model Object----> Single data type.
def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializers(stu)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data)
    return JsonResponse(serializer.data)

def student_details(request):
    stu=Student.objects.all()
    serializer=StudentSerializers(stu, many=True)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(serializer.data)
    return JsonResponse(serializer.data,safe=False)

# Deserializations
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer = StudentSerializers(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data inserted'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
