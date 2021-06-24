# Generated by Django 3.2.4 on 2021-06-24 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_question_user_mark_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair_programmer',
            name='user_1',
            field=models.ForeignKey(db_column='user_1', on_delete=django.db.models.deletion.CASCADE, related_name='pair_programmer_user_1', to='webapp.user'),
        ),
        migrations.AlterField(
            model_name='pair_programmer',
            name='user_2',
            field=models.ForeignKey(db_column='user_2', on_delete=django.db.models.deletion.CASCADE, related_name='pair_programmer_user_2', to='webapp.user'),
        ),
    ]
