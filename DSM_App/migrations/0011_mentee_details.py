# Generated by Django 4.1.5 on 2023-03-27 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DSM_App', '0010_mentee_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='mentee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_or_not', models.CharField(max_length=200, null=True)),
                ('visiting_home', models.CharField(max_length=200, null=True)),
                ('stay_details', models.CharField(max_length=200, null=True)),
                ('conveyance', models.CharField(max_length=200, null=True)),
                ('entrance_rank', models.CharField(max_length=200, null=True)),
                ('experience', models.CharField(max_length=200, null=True)),
                ('extra_curricular', models.CharField(max_length=200, null=True)),
                ('language', models.CharField(max_length=200, null=True)),
                ('achievements', models.CharField(max_length=200, null=True)),
                ('personal_goal', models.CharField(max_length=200, null=True)),
                ('professional_goal', models.CharField(max_length=200, null=True)),
                ('social_goal', models.CharField(max_length=200, null=True)),
                ('strength', models.CharField(max_length=200, null=True)),
                ('weakness', models.CharField(max_length=200, null=True)),
                ('opportunity', models.CharField(max_length=200, null=True)),
                ('threats', models.CharField(max_length=200, null=True)),
                ('hobbies', models.CharField(max_length=200, null=True)),
                ('role_model', models.CharField(max_length=200, null=True)),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='DSM_App.student_reg')),
            ],
        ),
    ]
