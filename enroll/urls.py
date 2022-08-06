from unicodedata import name
from django.urls import path
from .views import add_show, add_update, dele
urlpatterns = [
    
    path('',add_show,name="addandshow"),
    path('delete/<int:id>/',dele,name="delete_show"),
    path('<int:id>/',add_update,name="update")
]