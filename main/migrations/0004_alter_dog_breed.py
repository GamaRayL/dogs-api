# Generated by Django 4.2.6 on 2023-11-01 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_dog_options_rename_nickname_dog_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(blank=True, default='неизвестная порода', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dog', to='main.breed'),
        ),
    ]
