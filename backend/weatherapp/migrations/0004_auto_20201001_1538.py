# Generated by Django 2.2.16 on 2020-10-01 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0003_locations_cloudiness'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cloudiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum', models.CharField(max_length=256)),
                ('maximum', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='locations',
            name='cloudiness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations_cloudiness', to='weatherapp.Cloudiness'),
        ),
    ]
