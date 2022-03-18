from django.shortcuts import render
# from django.http import JsonResponse
from django.http import HttpResponse
def profile(request, input):
    return HttpResponse('<h1> 2 times of {} is {} </h1>'.format(input,input*2))