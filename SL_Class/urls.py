from django.urls  import path


from . import views

app_name = "SL_Class"

urlpatterns = [
    path('page=<int:page_number>/', views.MainView.as_view(), name='common'),
    path('ep/', views.IndexView.as_view(), name='index'),
    path('create_post/', views.CreateCView.as_view(), name='create_post'),
    path('about=<int:pk>', views.AboutView.as_view(), name='about'),
    path('delete=<int:pk>', views.DeleteCView.as_view(), name='delete'),
    path('change=<int:pk>', views.ChangeView.as_view(), name='change'),
    # path('page=<int:page_number>/', views.common, name='common'),
    # path('ep/', views.index, name='index'),
    # path('create_post/', views.create_post, name='create_post'),
    # path('about=<int:name_id>/', views.about, name='about'),
    # path('delete=<int:name_id>/', views.delete, name='delete'),
    # path('change=<int:name_id>/', views.change, name='change'),
]