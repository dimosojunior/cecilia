from django.urls import path
from .import views



urlpatterns = [

   
    path('home/', views.home, name="home"),
    
    path('base/', views.base, name="base"),
    path('add_student_report/', views.add_student_report, name="add_student_report"),
    path('sending_email/', views.sending_email, name="sending_email"),
    path('update_report/<str:pk>', views.update_report.as_view(), name="update_report"),
    path('delete_report/<int:pk>/', views.delete_report, name="delete_report"),
    path('view_report/<int:pk>/', views.view_report.as_view(), name="view_report"),
    path('', views.user_login, name="user_login"),
    path('user_registe/r', views.user_register, name="user_register"),
    path('user_logout/', views.user_logout, name="user_logout"),
    #path('search_report/', views.search_report, name="search_report"),

    path('search_autoco_report', views.search_autoco_report, name="search_autoco_report"),


    
  
  
   
   

 
    
    
 
    
 
]