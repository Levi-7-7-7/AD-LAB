from django.urls import path
from .import views

urlpatterns=[   
    path('',views.students,name='students'),
    path('details/<int:id>',views.details,name='details'),
    path('entry', views.student_entry, name='entry'),
    path('success', views.success_page, name='success'),   
]