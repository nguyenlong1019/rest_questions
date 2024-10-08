# Generated by Django 4.2.9 on 2024-09-23 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tên môn')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả môn học')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('true_answer', models.CharField(max_length=255, verbose_name='Đáp án đúng')),
                ('false_answer1', models.CharField(max_length=255, verbose_name='Đáp án sai 1')),
                ('false_answer2', models.CharField(max_length=255, verbose_name='Đáp án sai 2')),
                ('false_answer3', models.CharField(max_length=255, verbose_name='Đáp án sai 3')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='core.subject')),
            ],
        ),
    ]
