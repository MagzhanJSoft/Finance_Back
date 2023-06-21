# Generated by Django 4.1.2 on 2023-06-19 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dirs', '0005_organization_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='abp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='funcgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='funcpodgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
                ('_funcgroup', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.funcgroup', verbose_name='Фнкциональная группа')),
            ],
        ),
        migrations.CreateModel(
            name='specexp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
                ('_funcgroup', models.BigIntegerField(blank=True, null=True)),
                ('_abp', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.abp', verbose_name='АБП')),
                ('_funcpodgroup', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.funcpodgroup', verbose_name='АБП')),
            ],
        ),
        migrations.CreateModel(
            name='podprogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
                ('_funcgroup', models.BigIntegerField(blank=True, null=True)),
                ('_funcpodgroup', models.BigIntegerField(blank=True, null=True)),
                ('_abp', models.BigIntegerField(blank=True, null=True)),
                ('_program', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.program', verbose_name='АБП')),
            ],
        ),
        migrations.CreateModel(
            name='fkr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(null=True)),
                ('name_kaz', models.TextField(null=True)),
                ('name_rus', models.TextField(null=True)),
                ('_funcgroup', models.BigIntegerField(blank=True, null=True)),
                ('_funcpodgroup', models.BigIntegerField(blank=True, null=True)),
                ('_abp', models.BigIntegerField(blank=True, null=True)),
                ('_program', models.BigIntegerField(blank=True, null=True)),
                ('_podprogram', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dirs.podprogram', verbose_name='Фнкциональная группа')),
            ],
        ),
    ]
