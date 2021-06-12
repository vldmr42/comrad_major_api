# Generated by Django 2.2.10 on 2021-04-25 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0001_initial'),
        ('interrogations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(default=0)),
                ('chosen_answer', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='questions.OptionAnswer')),
                ('interrogation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interrogations.Interrogation')),
                ('written_answer', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='questions.TextAnswer')),
            ],
        ),
    ]
