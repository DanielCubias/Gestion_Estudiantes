# Generated by Django 4.2 on 2025-03-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('surname', models.CharField(max_length=500)),
                ('surname2', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('curs', models.EmailField(max_length=500)),
                ('tutor', models.CharField(max_length=500)),
                ('moduls_repartits', models.DateField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.RenameField(
            model_name='alumne',
            old_name='edat',
            new_name='curs',
        ),
        migrations.RenameField(
            model_name='alumne',
            old_name='genere',
            new_name='surname2',
        ),
        migrations.AddField(
            model_name='alumne',
            name='modulsMatriculats',
            field=models.CharField(default='valor_por_defecto', max_length=255),
        ),
    ]
