from django.urls import path
from .views import predict_species

urlpatterns = [
    path("", predict_species, name="predict"),
]
