from django.urls import path,include
from .views import *
from users.views import *
urlpatterns = [
    path('get-all-students',GetStudentView.as_view()),
    path('get-and-save-orders',GetOrdersViews.as_view()),
    path('delete-student/<int:pk>',DeleteStudentView.as_view()),
    path('students-details-address/<int:pk>',StudentsDetailsAddressViews.as_view()),
    path('Students-address-delete/<int:pk>',StudentsAddressDeleteViews.as_view())
]