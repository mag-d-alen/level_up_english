# Generated by Django 4.2 on 2023-05-01 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('silky', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestQuestionModel',
            new_name='TestQuestion',
        ),
        migrations.CreateModel(
            name='TestAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('test_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='silky.testquestion')),
            ],
        ),
    ]