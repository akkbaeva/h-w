# Generated by Django 3.2 on 2021-04-20 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(null=True, upload_to='comments/'),
        ),
    ]