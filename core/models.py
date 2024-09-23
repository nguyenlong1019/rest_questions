from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tên môn')
    description = models.TextField(blank=True, null=True, verbose_name='Mô tả môn học')

    def __str__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    true_answer = models.CharField(max_length=255, verbose_name='Đáp án đúng')
    false_answer1 = models.CharField(max_length=255, verbose_name='Đáp án sai 1')
    false_answer2 = models.CharField(max_length=255, verbose_name='Đáp án sai 2')
    false_answer3 = models.CharField(max_length=255, verbose_name='Đáp án sai 3')

    def __str__(self):
        return self.question_text
