from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Url
from django.shortcuts import redirect

# Create your views here.

def square(request):
    uni = get_random_string(length=50)

    return HttpResponse(uni)

@api_view(['POST'])
def rectangle(request):
    u=request.data [ 'url']
    uni_url = get_random_string(length=10)
    obj = Url(url=u, short_url=uni_url)
    obj.save()

    return Response ("127.0.0.1:8000/rrb/"+uni_url)

def circle(request,short):
    data = Url.objects.get(short_url=short)
    data.url

    return redirect(data.url)