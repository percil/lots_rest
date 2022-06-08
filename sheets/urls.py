from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import sheets.views as views

urlpatterns = [

    path('templates', views.GameTemplateListView.as_view()),
    path('sessions', views.GameSessionListView.as_view()),
    path('sessions/<int:id>', views.GameSessionDetailsView.as_view()),
    path('sheets', views.CharacterSheetListView.as_view()),
    path('sheets/<str:slug>', views.CharacterSheetView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
