# Generated by Django 4.2.2 on 2023-06-29 15:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('position_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='web.genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('hire_date', models.DateField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child', to='web.employee', verbose_name='Руководитель')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.position')),
            ],
        ),
    ]