from typing import Any

from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.views import View


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.urls import reverse

from Solo_Leveling.models import GVideo
from .forms import Create

from Solo_Leveling.func import validate_url

# Create your views here.

@method_decorator(login_required, name='dispatch')
class MainView(TemplateView):
    template_name = "SL_Class/common.html"
    paginate_by = 6
    
    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        paginator = Paginator(GVideo.objects.order_by("publish_date"), per_page=6, orphans=2)
        page_obj = paginator.get_page(kwargs.get("page_number"))


        page_addition_two = page_obj.number + 2
        if page_addition_two > paginator.num_pages:
            page_addition_two = 0

        page_negative_two = page_obj.number - 2
        if page_negative_two <= 0:
            page_negative_two = 0
        
        
        context.update({"page_obj": page_obj,
                        "page_number": page_obj.number,
                        "page_addition_two": page_addition_two,
                        "page_negative_two": page_negative_two})

        return context


class IndexView(TemplateView):
    template_name = "SL_Class/index.html"


class CreateCView(CreateView):
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



class AboutView(TemplateView):
    template_name = "SL_Class/about.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["video"] = GVideo.objects.get(pk=kwargs['pk'])
        return context
    

class DeleteCView(DeleteView):
    template_name = "SL_Class/confirm_for_delete.html"
    success_url = reverse_lazy("SL_Class:common", kwargs={"page_number": 1})
    model = GVideo

    def get_success_url(self) -> str:
        return self.success_url  # Повертає успішний URL

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        video = self.object  # `self.object` вже містить об'єкт GVideo
        context["video"] = video
        return context
    
    

class ChangeView(UpdateView):
    success_url = reverse_lazy("SL_Class:common", kwargs={"page_number": 1})
    template_name = "SL_Class/change.html"
    form_class = Create
    model = GVideo
    def get_success_url(self) -> str:
        return self.success_url
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        print(context["form"])
        context.update(kwargs)
        return context