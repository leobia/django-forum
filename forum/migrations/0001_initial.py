# Generated by Django 2.1.5 on 2019-01-21 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=120)),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('autore_discussione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussioni', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Discussione',
                'verbose_name_plural': 'Discussioni',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenuto', models.TextField()),
                ('data_creazione', models.DateTimeField(auto_now_add=True)),
                ('autore_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('discussione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Discussione')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Sezione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_sezione', models.CharField(max_length=80)),
                ('descrizione', models.CharField(blank=True, max_length=200, null=True)),
                ('logo_sezione', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Sezione',
                'verbose_name_plural': 'Sezioni',
            },
        ),
        migrations.AddField(
            model_name='discussione',
            name='sezione_appartenenza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussioni', to='forum.Sezione'),
        ),
    ]
