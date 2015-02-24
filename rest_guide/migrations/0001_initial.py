# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='modified date')),
            ],
        ),
        migrations.CreateModel(
            name='BookPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='modified date')),
                ('book', models.ForeignKey(to='rest_guide.Book')),
                ('book_part', models.ForeignKey(to='rest_guide.BookPart')),
            ],
        ),
        migrations.CreateModel(
            name='ElementAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(verbose_name='attribute data')),
            ],
        ),
        migrations.CreateModel(
            name='ElementAttributeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='modified date')),
            ],
        ),
        migrations.AddField(
            model_name='elementattributes',
            name='attribute_type',
            field=models.ForeignKey(to='rest_guide.ElementAttributeType'),
        ),
        migrations.AddField(
            model_name='elementattributes',
            name='element',
            field=models.ForeignKey(to='rest_guide.Element'),
        ),
        migrations.AddField(
            model_name='book',
            name='theme',
            field=models.ForeignKey(to='rest_guide.Theme'),
        ),
    ]
