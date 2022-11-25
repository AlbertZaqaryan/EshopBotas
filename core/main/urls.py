from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('botas/<int:id>/', Botas.as_view(), name='botas'),
    path('login/', LoginListView.as_view(), name='login'),
]