# Generated by Django 4.2.2 on 2023-08-12 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_catolog_id_catolog_alter_product_id_catolog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='product',
        ),
        migrations.CreateModel(
            name='Product_Block_SC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_product', models.IntegerField()),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.shopping_cart')),
            ],
        ),
    ]
