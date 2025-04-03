# Generated by Django 5.1.7 on 2025-04-01 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending', max_length=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
