from django.http import JsonResponse, Http404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Subject, Question

@method_decorator(csrf_exempt, name='dispatch')
class SubjectList(View):
    def get(self, request):
        subjects = list(Subject.objects.values())  # Lấy tất cả Subject dưới dạng dictionary
        return JsonResponse(subjects, safe=False)  # Trả về raw JSON

    def post(self, request):
        try:
            data = json.loads(request.body)  # Lấy dữ liệu từ request body
            subject = Subject.objects.create(name=data['name'], description=data.get('description', ''))
            return JsonResponse({'id': subject.id, 'name': subject.name, 'description': subject.description}, status=201)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class SubjectDetail(View):
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subject = self.get_object(pk)
        return JsonResponse({'id': subject.id, 'name': subject.name, 'description': subject.description})

    def put(self, request, pk):
        subject = self.get_object(pk)
        try:
            data = json.loads(request.body)
            subject.name = data.get('name', subject.name)
            subject.description = data.get('description', subject.description)
            subject.save()
            return JsonResponse({'id': subject.id, 'name': subject.name, 'description': subject.description})
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        subject.delete()
        return JsonResponse({}, status=204)

@method_decorator(csrf_exempt, name='dispatch')
class QuestionList(View):
    def get(self, request):
        questions = list(Question.objects.values())  # Lấy tất cả Question dưới dạng dictionary
        return JsonResponse(questions, safe=False)  # Trả về raw JSON

    def post(self, request):
        try:
            data = json.loads(request.body)
            question = Question.objects.create(
                subject_id=data['subject'],
                question_text=data['question_text'],
                true_answer=data['true_answer'],
                false_answer1=data['false_answer1'],
                false_answer2=data['false_answer2'],
                false_answer3=data['false_answer3']
            )
            return JsonResponse({
                'id': question.id,
                'subject': question.subject_id,
                'question_text': question.question_text,
                'true_answer': question.true_answer,
                'false_answer1': question.false_answer1,
                'false_answer2': question.false_answer2,
                'false_answer3': question.false_answer3,
            }, status=201)
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class QuestionDetail(View):
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        return JsonResponse({
            'id': question.id,
            'subject': question.subject_id,
            'question_text': question.question_text,
            'true_answer': question.true_answer,
            'false_answer1': question.false_answer1,
            'false_answer2': question.false_answer2,
            'false_answer3': question.false_answer3,
        })

    def put(self, request, pk):
        question = self.get_object(pk)
        try:
            data = json.loads(request.body)
            question.subject_id = data.get('subject', question.subject_id)
            question.question_text = data.get('question_text', question.question_text)
            question.true_answer = data.get('true_answer', question.true_answer)
            question.false_answer1 = data.get('false_answer1', question.false_answer1)
            question.false_answer2 = data.get('false_answer2', question.false_answer2)
            question.false_answer3 = data.get('false_answer3', question.false_answer3)
            question.save()
            return JsonResponse({
                'id': question.id,
                'subject': question.subject_id,
                'question_text': question.question_text,
                'true_answer': question.true_answer,
                'false_answer1': question.false_answer1,
                'false_answer2': question.false_answer2,
                'false_answer3': question.false_answer3,
            })
        except (KeyError, ValueError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return JsonResponse({}, status=204)
