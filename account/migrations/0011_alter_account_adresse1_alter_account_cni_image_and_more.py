# Generated by Django 4.2.1 on 2023-05-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_account_is_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='adresse1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='cni_image',
            field=models.FileField(upload_to='account/files/verification'),
        ),
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='justif_dom',
            field=models.FileField(upload_to='account/files/verification'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='account',
            name='pays',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='selfie',
            field=models.FileField(upload_to='account/files/verification'),
        ),
    ]
