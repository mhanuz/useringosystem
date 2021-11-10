# Generated by Django 2.0.1 on 2021-11-10 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=30)),
                ('post_code', models.PositiveIntegerField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.District')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Division')),
            ],
        ),
        migrations.CreateModel(
            name='PoliceStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.District')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Division')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='policstation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.PoliceStation'),
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Division'),
        ),
    ]
