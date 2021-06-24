# Generated by Django 3.2.4 on 2021-06-24 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_topic_id_questions_topic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='topic',
            new_name='topic_id',
        ),
        migrations.AlterField(
            model_name='questions',
            name='topic_id',
            field=models.ForeignKey(db_column='topic_id', on_delete=django.db.models.deletion.CASCADE, to='webapp.topic'),
        ),
    ]
