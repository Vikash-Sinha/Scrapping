from .import views
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('new-xls-file', NewXlsFile.as_view(), name="new_xls_file"),
    path('deldata', delQuery, name="delete"),
    ]