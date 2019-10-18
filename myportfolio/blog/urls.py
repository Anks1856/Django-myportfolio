from django.urls import path,include
from .import views


urlpatterns = [
        path('blog/',views.allblogs,name="allblogs"),
        path('blog/<int:blog_id>/',views.detail,name="detail"),
]