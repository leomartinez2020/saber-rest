from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from saber11 import views

urlpatterns = [
    path('colegios/', views.ColegioList.as_view()),
    path('colegios/<int:pk>/', views.ColegioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
