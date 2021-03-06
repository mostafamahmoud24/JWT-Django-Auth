# Generated by Django 3.2 on 2021-04-27 09:31

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.CharField(choices=[('Salamtak', 'Salamtak'), ('Risk', 'Risk'), ('Finance', 'Finance'), ('AML', 'AML'), ('OPS', 'OPS')], default='Risk', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permission',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Salamtak', 'Salamtak'), ('Risk', 'Risk'), ('Finance', 'Finance'), ('AML', 'AML'), ('OPS', 'OPS')], max_length=29),
        ),
    ]
