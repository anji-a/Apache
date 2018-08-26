# Generated by Django 2.0.1 on 2018-03-01 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MM', '0003_auto_20180225_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mpm_element',
            old_name='MPM_createddatetime',
            new_name='element_createddatetime',
        ),
        migrations.RenameField(
            model_name='mpm_element',
            old_name='MPM_type',
            new_name='element_displayname',
        ),
        migrations.RenameField(
            model_name='mpm_element',
            old_name='MPM_name',
            new_name='element_name',
        ),
        migrations.RenameField(
            model_name='mpm_element',
            old_name='MPM_stream',
            new_name='element_stream',
        ),
        migrations.RenameField(
            model_name='mpm_element',
            old_name='MPM_updatedatetime',
            new_name='element_updatedatetime',
        ),
        migrations.AddField(
            model_name='mpm_element',
            name='element_mode',
            field=models.CharField(default='Development', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mpm_element',
            name='element_type',
            field=models.CharField(default='Development', max_length=50),
            preserve_default=False,
        ),
    ]
