from django.urls import path
from .views import SubjectList, SubjectDetail, QuestionList, QuestionDetail

urlpatterns = [
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
]
