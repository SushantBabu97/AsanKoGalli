# Generated by Django 2.1.5 on 2019-02-01 02:46

import autoslug.fields
import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5)),
                ('details', ckeditor.fields.RichTextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('shart_intro', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('discount_price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('additional_information', ckeditor.fields.RichTextField()),
                ('best_seller', models.BooleanField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sale', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductHasImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductHasReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]