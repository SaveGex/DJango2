from django.shortcuts import render

from .models import GVideo

# Create your views here.
def common(request):
    list_urls = GVideo.objects.order_by("-url_video").values_list('url_video', flat=True)
    context = {
        "urls": list_urls
    }
    return render(request, "SL/common.html", context)


def index(request):
    return render(request, "SL/index.html")