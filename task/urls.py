from django.urls import path, include
from .views import *


urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('get-data/', GetRandomUserData.as_view(), name="get_data"),
    path('details-data/', Index.as_view, name='details-data'),
]
