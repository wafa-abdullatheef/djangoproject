from django.urls import path
from . import views
app_name='app18'
urlpatterns=[
    path('',views.index,name='index'),
    path('Signup',views.signup,name='Signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>/',views.home,name='home'),
    path('showusers',views.showusers,name='showusers'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('changepassword/<int:id>/',views.changepassword,name='changepassword'),
    path('logout',views.logout,name='logout'),
    path('gallery',views.gallery,name='gallery'),
    path('showimages',views.showimages,name='showimages'),
    path('mail',views.mail,name='mail'),
 
    
]