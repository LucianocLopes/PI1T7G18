# Generated by Django 5.0.6 on 2024-05-10 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduation', '0002_alter_discipline_disciplines'),
        ('group', '0001_initial'),
        ('teacher', '0002_alter_teacher_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayGridGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_start', models.TimeField(verbose_name='Horário de inicio')),
            ],
            options={
                'verbose_name': 'DayGridGroup',
                'verbose_name_plural': 'DayGridGroups',
            },
        ),
        migrations.CreateModel(
            name='GridGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval_start', models.TimeField(verbose_name='Inicio do Intervalo')),
                ('interval_duration', models.DurationField(verbose_name='Duração do Intervalo')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='group.group', verbose_name='Classe')),
            ],
            options={
                'verbose_name': 'GridGroup',
                'verbose_name_plural': 'GridGroups',
            },
        ),
        migrations.CreateModel(
            name='HourGridGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diration', models.DurationField(verbose_name='Duaração')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.daygridgroup', verbose_name='Horário da Grade Escolar')),
                ('dicipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='graduation.discipline', verbose_name='Disciplina')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='Professor')),
            ],
            options={
                'verbose_name': 'WeekGridGroup',
                'verbose_name_plural': 'WeekGridGroups',
            },
        ),
        migrations.CreateModel(
            name='WeekGridGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(verbose_name='Data Inicio da Semana')),
                ('grid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.gridgroup', verbose_name='Grade Escolar')),
            ],
            options={
                'verbose_name': 'WeekGridGroup',
                'verbose_name_plural': 'WeekGridGroups',
            },
        ),
        migrations.AddField(
            model_name='daygridgroup',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.weekgridgroup', verbose_name='Semana da Grade Escolar'),
        ),
    ]
