# Generated by Django 4.0 on 2021-12-30 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(blank=True, max_length=333, null=True)),
                ('brand', models.CharField(blank=True, max_length=333, null=True)),
                ('category', models.CharField(blank=True, max_length=333, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField()),
                ('numReviews', models.IntegerField(blank=True, default=0, null=True)),
                ('price', models.IntegerField()),
                ('countInStock', models.IntegerField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user')),
            ],
        ),
    ]
