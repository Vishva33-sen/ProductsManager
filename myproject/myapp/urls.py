from . import views
from django.urls import path

urlpatterns=[
    path('',views.home,name='home'),
    path('myapp/<str:t>/',views.myapp,name='myapp'),
    path('types/',views.getTypes,name='types'),
]