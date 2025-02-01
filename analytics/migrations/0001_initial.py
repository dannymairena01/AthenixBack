# Generated by Django 5.1.5 on 2025-01-30 23:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('risk_of_injury', models.FloatField()),
                ('recommendations', models.TextField()),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analysis_results', to='athletes.athlete')),
            ],
        ),
    ]
