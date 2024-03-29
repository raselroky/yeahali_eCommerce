# Generated by Django 5.0 on 2024-02-06 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('product_description', models.TextField(blank=True, help_text='shortly full details for product and explain size,color,qunatity etc', null=True)),
                ('product_image', models.FileField(blank=True, null=True, upload_to='product_image/')),
                ('product_price', models.TextField(blank=True, null=True)),
                ('contact_me', models.TextField(blank=True, help_text='email, number, social_link or any details for contact', null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('product_brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.brand')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('product_subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Image_Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.add_product')),
            ],
        ),
    ]
