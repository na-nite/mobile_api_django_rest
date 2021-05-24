# Generated by Django 3.0.6 on 2020-06-17 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0003_country_drapeau_carre'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='capital',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='SlideShowImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slideShow')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fonction', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='slideShow')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='country.Country')),
            ],
        ),
    ]
