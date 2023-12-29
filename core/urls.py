from django.urls import path
# from .views import index, contato, form_modelform
from .views import index, contato, formulario


urlpatterns = [
    path('', index),   
    path('formulario/', formulario, name='formulario')
]