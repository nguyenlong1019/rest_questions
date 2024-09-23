from django.contrib import admin
from .models import Subject, Question

# Tạo một Inline cho Question
class QuestionInline(admin.TabularInline): 
    model = Question
    extra = 4  # Số lượng dòng trống cho phép thêm câu hỏi mới

# Đăng ký Subject cùng với QuestionInline
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    inlines = [QuestionInline]


# Đăng ký thêm Question để có thể quản lý độc lập nếu cần thiết
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ('subject', 'question_text', 'true_answer')

