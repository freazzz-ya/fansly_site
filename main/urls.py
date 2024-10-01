from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
       path('', views.list_view, name='list_view'), 
       # ... other paths if needed
]