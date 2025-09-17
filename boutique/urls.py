from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_sacs, name='liste_sacs'),
    path('<int:sac_id>/', views.detail_sac, name='detail_sac'),
]