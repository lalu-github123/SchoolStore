# Generated by Django 4.2.3 on 2023-07-27 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SSapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purposes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField(default='1996-09-3')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('trans', 'Trans')], max_length=25)),
                ('phone_number', models.IntegerField()),
                ('mail', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('materials_provide_1', models.BooleanField(default=False, verbose_name='Debit Note')),
                ('materials_provide_2', models.BooleanField(default=False, verbose_name='Pen')),
                ('materials_provide_3', models.BooleanField(default=False, verbose_name='Exam Papers')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SSapp.courses')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SSapp.department')),
                ('purpose', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='SSapp.purposes')),
            ],
        ),
    ]
