from django.urls import path
from .views import *

urlpatterns = [
    path('all', AllView.as_view()),
    path('view/<str:id>', ViewView.as_view()),
    path('add', AddView.as_view()),
    path('update', UpdateView.as_view()),
    path('delete/<str:id>', DeleteView.as_view()),
]