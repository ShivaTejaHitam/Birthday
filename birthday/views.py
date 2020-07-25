from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy
from . forms import MemoriesForm,VideosForm,StoriesForm,UserForm
from django.views.generic import DeleteView
from . models import Memories,Videos,Stories,Jayanth
import os


def memories(request):
    memor=Memories.objects.all()
    current_user=request.session.get('user_ses',None)
    return render(request,'birthday/memories.html',{'memor':memor,'current_user':current_user})    

def videos(request):
    memor=Videos.objects.all()
    current_user=request.session.get('user_ses',None)
    return render(request,'birthday/videos.html',{'memor':memor,'current_user':current_user})

def stories(request):
    memor=Stories.objects.all()
    current_user=request.session.get('user_ses',None)
    return render(request,'birthday/stories.html',{'memor':memor,'current_user':current_user})

def about(request):
    current_user=request.session.get('user_ses',None)
    return render(request,'birthday/about.html',{'current_user':current_user})

def home(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            e=form.cleaned_data['email']
            p=form.cleaned_data['password']
            yes=Jayanth.objects.filter(email=e)
            if yes.exists():
                request.session['user_ses']=e
                current_user=request.session['user_ses']
                return render(request,'birthday/index.html',{'current_user':current_user})
            else:
                err="User Doesn't exist"
                return render(request,'birthday/index.html',{'err':err,'form':form})
        else:
            err="Check Your Fields"
            return render(request,'birthday/index.html',{'err':err,'form':form})
    else:
        form=UserForm()
        current_user=request.session.get('user_ses',None)
    return render(request,'birthday/index.html',{'form':form,'current_user':current_user})

def addmemories(request):
    if request.session.get('user_ses',None):
        if request.method=='POST':
            form=MemoriesForm(request.POST,request.FILES)
            if form.is_valid():
                t=form.cleaned_data['title']
                i=form.cleaned_data['image']
                record=Memories(title=t,image=i)
                record.save()
                return HttpResponseRedirect(reverse('memories'))
            else:
                field_error="please check the fields"
                return render(request,'birthday/memories_form.html',{'form':form,'field_error':field_error})
        else:
            form=MemoriesForm()
        return render(request,'birthday/memories_form.html',{'form':form})
    else:
        return  HttpResponseRedirect(reverse('memories'))

def addvideos(request):
    if request.session.get('user_ses',None):
        if request.method=='POST':
            form=VideosForm(request.POST,request.FILES)
            if form.is_valid():
                t=form.cleaned_data['title']
                i=form.cleaned_data['video']
                record=Videos(title=t,video=i)
                record.save()
                return HttpResponseRedirect(reverse('videos'))
            else:
                field_error="please check the fields"
                return render(request,'birthday/videoform.html',{'form':form,'field_error':field_error})
        else:
            form=MemoriesForm()
        return render(request,'birthday/videoform.html',{'form':form})
    else:
        return  HttpResponseRedirect(reverse('videos'))


def addstories(request):
    if request.session.get('user_ses',None):
        if request.method=='POST':
            form=StoriesForm(request.POST)
            if form.is_valid():
                t=form.cleaned_data['title']
                i=form.cleaned_data['Story']
                record=Stories(title=t,Story=i)
                record.save()
                return HttpResponseRedirect(reverse('stories'))
            else:
                field_error="please check the fields"
                return render(request,'birthday/storyform.html',{'form':form,'field_error':field_error})
        else:
            form=StoriesForm()
        return render(request,'birthday/storyform.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('stories'))


def DeleteStory(request,s_id):
    record=Stories.objects.filter(id=s_id)
    record.delete()
    return HttpResponseRedirect(reverse('stories'))
    

def DeleteMemory(request,m_id):
    record=Memories.objects.get(id=m_id)
    record.image.delete()
    record.delete()
    return HttpResponseRedirect(reverse('memories'))
    


def DeleteVideo(request,v_id):
    record=Videos.objects.get(id=v_id)
    record.video.delete()
    record.delete()
    return HttpResponseRedirect(reverse('videos'))
    
def logout(request):
    try:
        del request.session['user_ses']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('home'))