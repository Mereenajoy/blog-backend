import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from blog.serializer import *
from blog.models import *
from django.db.models import *


@csrf_exempt
def addPost(request):
    if request.method =="POST":
        recieved_data = json.loads(request.body)
        print(recieved_data)
        serialized_check = PostSerializer(data=recieved_data)
        if serialized_check.is_valid():
            serialized_check.save()
            return HttpResponse(json.dumps({"status" : "added"}))
        else:
            return HttpResponse(json.dumps({"status" : "failed"}))

    
@csrf_exempt
def searchPost(request):
    if request.method =="POST":
        recieved_data = json.loads(request.body)
        getTitle =recieved_data["title"]
        data = list(PostModel.objects.filter(Q(title__icontains=getTitle)).values())
        return HttpResponse(json.dumps(data))
    else :
        return HttpResponse("invalid")

@csrf_exempt    
def viewPost(request):
    if request.method =="POST":
        blogList = PostModel.objects.all()
        newBlogList =PostSerializer(blogList , many=True)
        return HttpResponse(json.dumps(newBlogList.data))
