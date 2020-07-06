# Generated by Django 2.2.6 on 2020-06-28 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_remove_book_maker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maker',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='maker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='book_publish', to='p_library.Maker', verbose_name='Издательство'),
        ),
    ]