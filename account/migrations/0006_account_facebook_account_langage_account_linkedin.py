# Generated by Django 4.2.1 on 2023-05-25 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_activitee_account_adresse1_account_adresse2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='facebook',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='account',
            name='langage',
            field=models.CharField(choices=[('FRANCAIS', 'Français'), ('ANGLAIS', 'Anglais'), ('MALAGASY', 'Malagasy'), ('EMPTY', '---')], default='EMPTY', max_length=12),
        ),
        migrations.AddField(
            model_name='account',
            name='linkedin',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]