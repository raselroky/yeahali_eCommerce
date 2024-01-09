# Generated by Django 5.0 on 2024-01-09 08:13

import django_countries.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_All',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('last_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(help_text='adjust with country code', max_length=128, region=None, unique=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('date_of_joining', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('Select', 'Select'), ('Manufacture/Seller', 'Manufacture/Seller'), ('Buyer', 'Buyer'), ('Both', 'Both')], default='Select', max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('gender', models.CharField(choices=[('Select', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Select', max_length=1000)),
                ('marital_status', models.CharField(choices=[('Select', 'Select'), ('Married', 'Married'), ('Unmarried', 'Unmarried'), ('Others', 'Others')], default='Select', max_length=1000)),
                ('blood_group', models.CharField(blank=True, max_length=1000, null=True)),
                ('soacial_link', models.TextField(blank=True, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_address', models.CharField(blank=True, max_length=2000, null=True)),
                ('company_contact_number', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('bank_name', models.CharField(blank=True, max_length=2000, null=True)),
                ('card_or_account_number', models.TextField(blank=True, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]