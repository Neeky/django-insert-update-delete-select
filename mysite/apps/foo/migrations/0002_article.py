# Generated by Django 3.0 on 2020-02-01 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foo.Person')),
            ],
        ),
    ]
