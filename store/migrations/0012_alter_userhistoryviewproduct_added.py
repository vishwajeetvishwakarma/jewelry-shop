# Generated by Django 4.1.7 on 2023-03-16 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_review_content_alter_review_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistoryviewproduct',
            name='added',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 16, 21, 21, 36, 302400, tzinfo=datetime.timezone.utc)),
        ),
    ]
