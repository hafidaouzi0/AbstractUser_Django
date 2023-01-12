from django.urls import path,include
from . import views
urlpatterns = [
path("update/<int:pk>",views.update_user)
]