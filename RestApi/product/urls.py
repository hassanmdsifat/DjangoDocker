from django.urls import path
from .views import GetAllProducts


urlpatterns = [
    path('all/', GetAllProducts.as_view()),
]
