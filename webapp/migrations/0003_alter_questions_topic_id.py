# Generated by Django 3.2.4 on 2021-06-24 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_questions_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='topic_id',
            field=models.ForeignKey(db_column='name', on_delete=django.db.models.deletion.CASCADE, to='webapp.topic'),
        ),
    ]
