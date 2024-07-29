from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from .models import GVideo
from .forms import Create

# Create your views here.
def common(request):
    list_video = GVideo.objects.all()
    context = {
        "urls": list_video
    }
    return render(request, "SL/common.html", context)


def index(request):
    return render(request, "SL/index.html")


def create(request):
    return render(request, "SL/create.html", {"count": GVideo.objects.count(),})

def create_post(request):
    context = {
        "count": GVideo.objects.count(),
        "error_msg": "Error",
        "count": GVideo.objects.count(),
    }
    if request.method == "POST":
        form = Create(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post created successfully")
            return HttpResponseRedirect(reverse("SL:common"))
        else:
            return render(request, "SL/create.html", context)

    else:
        form = Create()
        return render(request, "SL/create.html", context)
    


def about(request, name_id):
    video = GVideo.objects.get(pk=name_id)
    context = {
        'video': video
    }
    return render(request, "SL/about.html", context)


def delete(request, name_id):
    video = GVideo.objects.get(pk=name_id)
    video.delete()
    return redirect("SL:common")
    # return HttpResponseRedirect(reverse("SL:common"))


def change(request, name_id):
    video = GVideo.objects.get(pk=name_id)
    name = ''
    comment_video = ''
    url_video = ''
    
    if request.method == "POST":
        form = Create(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect("SL:about", name_id)
        else:

            if request.POST.get("name") == "":
                name = "Name cannot be empty"
            if request.POST.get("comment_video") == "":
                comment_video = "Comment cannot be empty"
            if request.POST.get("url_video") == "":
                url_video = "URL cannot be empty"
            return render(request, "SL/change.html", {
                "video": video, 
                "name": name, 
                "comment_video": comment_video, 
                "url_video": url_video
            })

    return render(request, "SL/change.html", {"video": video})
