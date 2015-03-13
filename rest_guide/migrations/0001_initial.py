# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='modified date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookPart',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('section', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='modified date')),
                ('book', models.ForeignKey(to='rest_guide.Book')),
                ('book_part', models.ForeignKey(to='rest_guide.BookPart')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElementAttributes',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('data', models.TextField(verbose_name='attribute data')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElementAttributeType',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('label', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=25)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('mod_date', models.DateTimeField(verbose_name='modified date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='elementattributes',
            name='attribute_type',
            field=models.ForeignKey(to='rest_guide.ElementAttributeType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='elementattributes',
            name='element',
            field=models.ForeignKey(to='rest_guide.Element'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='theme',
            field=models.ForeignKey(to='rest_guide.Theme'),
            preserve_default=True,
        ),
    ]
