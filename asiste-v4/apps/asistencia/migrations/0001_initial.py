# Generated by Django 4.2.3 on 2023-08-01 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('documento_aprendiz', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cedula de ciudadanía'), ('TI', 'Tarjeta de identidad')], max_length=20)),
                ('nombres_aprendiz', models.CharField(max_length=45)),
                ('apellidos_aprendiz', models.CharField(max_length=45)),
                ('email_personal_aprendiz', models.CharField(max_length=45)),
                ('email_institucional_aprendiz', models.CharField(max_length=45)),
                ('numero_celular', models.IntegerField()),
                ('genero_aprendiz', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Homosexual', 'Homosexual'), ('Bisexual', 'Bisexual'), ('Transexual', 'Transexual')], max_length=10)),
            ],
            options={
                'verbose_name': 'Aprendiz',
                'verbose_name_plural': 'Aprendices',
                'ordering': ('-nombres_aprendiz',),
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asistencia', models.DateField(auto_now_add=True)),
                ('presente', models.CharField(choices=[('Asiste', 'Asiste'), ('Falla', 'Falla'), ('Novedad', 'Novedad')], default=False, max_length=45)),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
        migrations.CreateModel(
            name='Coordinacion',
            fields=[
                ('id_coordinacion', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre_coordinacion', models.CharField(choices=[('TELEINFORMATICA', 'Teleinformática')], max_length=45)),
            ],
            options={
                'verbose_name': 'Coordinacion',
                'verbose_name_plural': 'Coordinaciones',
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.IntegerField(primary_key=True, serialize=False)),
                ('nivel_formacion', models.CharField(choices=[('TECNICO', 'Técnico'), ('TECNOLOGO', 'Tecnologo'), ('COMPLEMENTARIO', 'Complementario')], max_length=20)),
            ],
            options={
                'verbose_name': 'Ficha',
                'verbose_name_plural': 'Fichas',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('horario_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('fecha', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('salon', models.IntegerField()),
                ('jornada', models.CharField(choices=[('DIURNA', 'Diurna'), ('TARDE', 'Tarde'), ('NOCTURNA', 'Nocturna')], max_length=10)),
                ('asignatura', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres_instructor', models.CharField(max_length=45)),
                ('apellidos_instructor', models.CharField(max_length=45)),
                ('email_institucional', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructores',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id_programa', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_programa', models.CharField(choices=[('ADSO', 'Analisis y desarrollo de software'), ('ADSI', 'Analisis y desarrollo de sistemas')], max_length=45)),
                ('coordinacion_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.coordinacion')),
            ],
            options={
                'verbose_name': 'Programa',
                'verbose_name_plural': 'Programas',
            },
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id_novedad', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_novedad', models.CharField(choices=[('Calamidad', 'Calamidad domestica'), ('Medica', 'Novedad medica')], max_length=10)),
                ('observaciones', models.TextField(max_length=30)),
                ('archivo_adjunto', models.FileField(upload_to='pdfs/')),
                ('estado_novedad', models.BooleanField(choices=[(True, 'Aceptada'), (False, 'No aceptada')], default=False)),
                ('aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.aprendiz')),
                ('asistencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.asistencia')),
            ],
            options={
                'verbose_name': 'Novedad',
                'verbose_name_plural': 'Novedades',
            },
        ),
    ]
