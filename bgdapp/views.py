from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseNotFound
from bgdapp.models import Story
from django import template

register = template.Library()

@register.filter(name='purpose')
def purpose(value, arg):
    return value.filter(purpose__title=arg)

@register.filter(name='mission')
def mission(value, arg):
    return value.filter(story__mission__title=arg)
    
def everything(request):
    stories = Story.objects.all().order_by('mission', '-priority')
    return render_to_response('everything.html', {'stories':stories} )
    
def content(request):
    content = Content.objects.all().order_by('mission', '-priority')
    return render_to_response('everything.html', {'content':content} )
    
    
    
    

