from django.urls import path
from . import views

urlpatterns = [
   path('registeruser/',views.registeruser, name="register"),
   path('',views.loginPage, name="loginPage"),
   path('logout',views.logoutUser, name="logout"),
   path('home',views.home, name="home"),
   path('sampleInput',views.sampleInput, name='sampleInput'),
   path('predict',views.predict, name='predict'),
   path('studadvise',views.studadvise, name="studadvise")
 #  path('loginstud/<str:pk_test>/', views.loginstud, name="loginstud")
   

]
