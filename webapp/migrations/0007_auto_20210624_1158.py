# Generated by Django 3.2.4 on 2021-06-24 11:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20210624_1140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.CreateModel(
            name='User_asked_for_pair_programming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='webapp.user_asked_for_pair_programming')),
            ],
        ),
        migrations.CreateModel(
            name='Question_user_mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(choices=[('pending', 0), ('need to revise', 1), ('done', 2)], validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('question_id', models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, to='webapp.question')),
                ('user_id', models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='webapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Pair_programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_1', models.ForeignKey(db_column='user_1', on_delete=django.db.models.deletion.CASCADE, related_name='pair_programmer_user_1', to='webapp.pair_programmer')),
                ('user_2', models.ForeignKey(db_column='user_2', on_delete=django.db.models.deletion.CASCADE, related_name='pair_programmer_user_2', to='webapp.pair_programmer')),
            ],
        ),
        migrations.CreateModel(
            name='Mark_update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_user_mark_id', models.ForeignKey(db_column='question_user_mark_id', on_delete=django.db.models.deletion.CASCADE, to='webapp.question_user_mark')),
            ],
        ),
    ]
