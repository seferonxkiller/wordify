# Generated by Django 4.1.5 on 2023-02-02 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_articletext_articleimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articleimage',
            name='article',
        ),
        migrations.AddField(
            model_name='articleimage',
            name='article_text',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.articletext'),
            preserve_default=False,
        ),
    ]
