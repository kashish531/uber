from django.urls import path,include
from .views import *
from users.views import *
urlpatterns = [
    path('get-all-students',GetStudentView.as_view()),
    path('get-and-save-orders',GetOrdersViews.as_view()),
]