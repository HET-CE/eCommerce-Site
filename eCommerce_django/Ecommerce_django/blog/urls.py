# from django.contrib import admin
# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('', views.index,name="BlogHome"),
#     path('blogpost/', views.blogpost,name="blogPost"),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogpost")
]
