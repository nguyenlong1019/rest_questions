from django.shortcuts import render

from rest_framework import viewsets
from .models import Subject, Question
from .serializers import SubjectSerializer, QuestionSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

