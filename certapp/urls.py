from django.urls import path
from . import views

urlpatterns = [
    # path('download-certificate/<int:enrolment_id>/', views.download_certificate, name='download_certificate'),
    path("",views.index,name="index"),
    path('verify-certificate/<str:code>/', views.verify_certificate, name='verify_certificate')

    
]