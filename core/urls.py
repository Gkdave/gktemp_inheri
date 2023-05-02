from django.urls import path 
from . import views 
urlpatterns = [
    path('',views.sonika,name='sonika'), 
    path('ras/',views.rashmi,name='rashmi'), 
    path('him/',views.himanshu,name='himanshu'), 
    path('ravi/',views.ravi,name='ravi'),  
    path('dishu/',views.dishu,name='dishu'),  
]
