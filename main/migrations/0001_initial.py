# Generated by Django 2.1.7 on 2019-03-27 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grammar_productions', models.TextField()),
                ('grammar_used_parser', models.CharField(max_length=20)),
                ('grammar_parsing_table_entries', models.TextField()),
                ('grammar_timestamp', models.DateTimeField(verbose_name='Date submitted')),
                ('grammar_user_submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
