from django.urls import path
 
from . import views  
 
urlpatterns = [
   path('mailfinder/', views.TextMailFinderAPIView.as_view(), name='text-mailfinder'),
   path('numberfinder/', views.NumberFinderAPIView.as_view(), name='text-numberfinder'),
   path('domainfinder/', views.DomainFinderAPIView.as_view(), name='text-domainfinder'),
   path('image/', views.ImageToTextAPIView.as_view(), name='image-to-text'),
   path('article/', views.AryticleWriterAPIView.as_view(), name='image-to-text'),
   path('grammer/', views.GrammerWriterAPIView.as_view(), name='image-to-text'),
]
