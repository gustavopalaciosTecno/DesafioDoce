# Generated by Django 4.2.2 on 2023-07-10 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='articulo',
            options={'ordering': ['-creacion']},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='etiqueta',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='actualizacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.usuario'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
