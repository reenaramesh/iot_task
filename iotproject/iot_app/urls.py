from django.urls import path, include
from iot_app import views 
 
urlpatterns = [ 
    path('api/device', views.device_list),
    #path('api/device1', views.device_detail),
    #path('api/device1/(?P<pk>[0-9]+)$', views.device_detail),
    path('api/device1/<int:device_id>', views.device_detail),
    
]