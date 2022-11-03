import imp
from django.urls import path
from api.views import test
# from . import views 
urlpatterns = [
    path('test', test.as_view(), name='test_api')
]
