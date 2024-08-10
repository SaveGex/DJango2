from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from django.contrib import messages
from Solo_Leveling.func import validate_url
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .forms import Create

# Create your views here.

# @login_required
# def common(request, page_number):
#     list_video = GVideo.objects.all()
#     paginator = Paginator(list_video, per_page=6, orphans=2)  # Show 25 contacts per page.
#     page_obj = paginator.get_page(page_number)
#     page_addition_two = page_obj.number + 2
#     if((page_addition_two<=paginator.num_pages) == False):
#         page_addition_two = 0
    
#     page_negative_two = page_obj.number - 2
#     if(page_negative_two<=0):
#         page_negative_two = 0
#     return render(request, "SL/common.html", context= {
#         "urls": list_video,
#         "page_obj": page_obj,
#         "page_number": page_number,
#         "page_addition_two": page_addition_two,
#         "page_negative_two": page_negative_two,
#     })


# def index(request):
#     return render(request, "SL/index.html")


# def create_post(request):
#     if request.method == "POST":
#         name = ''
#         comment_video = ''
#         url_video = ''
#         form_error = ''

#         if request.method == "POST":
#             form = Create(request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Post created successfully")
#                 return redirect("SL:common", page_number=1)  
#                 # return HttpResponseRedirect(reverse("SL:common", args=(1)))
#             else:
#                 video_data = {
#                     "name": request.POST["name"],
#                     "comment_video": request.POST["comment_video"],
#                     "url_video": request.POST["url_video"]
#                 }
#                 if request.POST["name"] == "":
#                     name = "Name cannot be empty"
#                 if request.POST["comment_video"] == "":
#                     comment_video = "Comment cannot be empty"
#                 if request.POST["url_video"] == "":
#                     url_video = "URL cannot be empty"
#                 if not validate_url(request.POST["url_video"]) and request.POST["url_video"] != "":
#                     form_error = "URL is not valid"
#                 print(form_error)
#                 return render(request, "SL/create.html", {
#                     "video": video_data, 
#                     "name": name, 
#                     "comment_video": comment_video, 
#                     "url_video": url_video,
#                     "form_error": form_error
#                 })
#     else:
#         return render(request, "SL/create.html")
    


# def about(request, name_id):
#     video = GVideo.objects.get(pk=name_id)
#     context = {
#         'video': video
#     }
#     return render(request, "SL/about.html", context)


# def delete(request, name_id):
#     video = GVideo.objects.get(pk=name_id)
#     video.delete()
#     return redirect("SL:common", page_number=1)
#     # return HttpResponseRedirect(reverse("SL:common"))


# def change(request, name_id):
#     video = GVideo.objects.get(pk=name_id)
#     name = ''
#     comment_video = ''
#     url_video = ''
    
#     if request.method == "POST":
#         form = Create(request.POST, instance=video)
#         if form.is_valid():
#             form.save()
#             return redirect("SL:about", name_id)
#         else:
#             video_data = {
#                 "name": request.POST["name"],
#                 "comment_video": request.POST["comment_video"],
#                 "url_video": request.POST["url_video"]
#             }
#             if request.POST["name"] == "":
#                 name = "Name cannot be empty"
#             if request.POST["comment_video"] == "":
#                 comment_video = "Comment cannot be empty"
#             if request.POST["url_video"] == "":
#                 url_video = "URL cannot be empty"
#             return render(request, "SL/change.html", {
#                 "video": video_data, 
#                 "name": name, 
#                 "comment_video": comment_video, 
#                 "url_video": url_video,
#                 "name_id": name_id
#             })
#     return render(request, "SL/change.html", {"video": video, "name_id": name_id})