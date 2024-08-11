from typing import Any

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from Solo_Leveling.func import validate_url
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse

from Solo_Leveling.models import GVideo
from .forms import Create

# Create your views here.

@method_decorator(login_required, name='dispatch')
class Main(TemplateView):
    template_name = "SL_Class/common.html"
    paginate_by = 6
    
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        paginator = Paginator(GVideo.objects.order_by("-publish_date"), per_page=6, orphans=2)
        page_obj = paginator.get_page(kwargs.get("page_number"))

        print(kwargs.get("page_number"))

        context["page_obj"] = page_obj
        context["page_number"] = page_obj.number

        
        page_addition_two = page_obj.number + 2
        if page_addition_two > paginator.num_pages:
            page_addition_two = 0

        page_negative_two = page_obj.number - 2
        if page_negative_two <= 0:
            page_negative_two = 0

        context["page_addition_two"] = page_addition_two
        context["page_negative_two"] = page_negative_two

        return context


class Index(TemplateView):
    template_name = "SL_Class/index.html"


class Create(CreateView):
    model = GVideo
    form_class = Create
    template_name = "SL_Class/create.html"
    success_url = reverse_lazy("SL_Class:common", kwargs = {'page_number': 1})

    def get_form_valid(self):
        messages.success(self.request, "Post created successfully")
        return reverse_lazy("SL_Class:common", kwargs = {"page_number": 1})
    def form_invalid(self, form, **kwargs):
        video_data = form.cleaned_data
        name = comment_video = url_video = form_error = ""


        if not video_data.get("name"):
            name = "Name cannot be empty"
        if not video_data.get("comment_video"):
            comment_video = "Comment cannot be empty"
        if not video_data.get("url_video"):
            url_video = "URL cannot be empty"
        if video_data.get("url_video") and not validate_url(video_data["url_video"]):
            form_error = "URL is not valid"



        context = super().get_context_data(form=form)
        context.update({
                "video": video_data,
                "name": name,
                "comment_video": comment_video,
                "url_video": url_video,
                "form_error": form_error
            })
            
        return self.render_to_response(context)

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