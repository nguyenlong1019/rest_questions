# serializers.py
from rest_framework import serializers
from .models import Subject, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'true_answer', 'false_answer1', 'false_answer2', 'false_answer3']

class SubjectSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'description', 'questions']
