# Generated by Django 4.2.5 on 2023-11-14 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asistencia', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='instructor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ficha',
            name='horario_ficha',
            field=models.ManyToManyField(to='asistencia.horariopordia'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='programa_ficha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.programa'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='aprendiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.aprendiz'),
        ),
        migrations.AddField(
            model_name='aprendiz',
            name='ficha_aprendiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.ficha'),
        ),
        migrations.AddField(
            model_name='aprendiz',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='aprendiz', to=settings.AUTH_USER_MODEL),
        ),
    ]
