from django.urls import path
from new import views

app_name = 'test'
urlpatterns = [
    path('test/', views.test_print, name='test_print'),
]