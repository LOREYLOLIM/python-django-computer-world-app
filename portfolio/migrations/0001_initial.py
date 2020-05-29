# Generated by Django 2.1.7 on 2020-05-29 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=200)),
                ('Statement', models.TextField()),
                ('Approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_Topic', models.CharField(max_length=200)),
                ('Book', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('Video', models.CharField(blank=True, max_length=100, null=True)),
                ('Uploaded_by', models.CharField(max_length=1000)),
                ('Date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.CharField(max_length=150)),
                ('Message', models.TextField(null=True)),
                ('contents', models.FileField(blank=True, default='upload', upload_to='uploaded_newsletters/')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Description', models.TextField()),
                ('Price', models.IntegerField()),
                ('Brand', models.CharField(choices=[('.all', 'All'), ('.computers', 'Computers'), ('.phones', 'Phones'), ('.Cameras', 'Cameras')], default='.all', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('conf_num', models.CharField(max_length=15)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Testimonial', models.TextField(max_length=500)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Approved_comment', models.BooleanField(default=False)),
            ],
        ),
    ]
