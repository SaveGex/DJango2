from django.urls  import path


from . import views

app_name = "SL"

urlpatterns = [
    path('page=<int:page_number>/', views.common, name='common'),
    path('ep/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create_post/', views.create_post, name='create_post'),
    path('about=<int:name_id>/', views.about, name='about'),
    path('delete=<int:name_id>/', views.delete, name='delete'),
    path('change=<int:name_id>/', views.change, name='change'),
]