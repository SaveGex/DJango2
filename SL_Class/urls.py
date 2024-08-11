from django.urls  import path


from . import views

app_name = "SL_Class"

urlpatterns = [
    path('page=<int:page_number>/', views.Main.as_view(), name='common'),
    path('ep/', views.Index.as_view(), name='index'),
    path('create_post/', views.Create.as_view(), name='create_post')
    # path('page=<int:page_number>/', views.common, name='common'),
    # path('ep/', views.index, name='index'),
    # path('create_post/', views.create_post, name='create_post'),
    # path('about=<int:name_id>/', views.about, name='about'),
    # path('delete=<int:name_id>/', views.delete, name='delete'),
    # path('change=<int:name_id>/', views.change, name='change'),
]