from django.urls import path
from .views import classify

app_name = 'classifier'

urlpatterns = [
    path('', classify, name='classify'),
]
