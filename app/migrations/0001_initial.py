
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TreeMenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('verbose_name', models.CharField(blank=True, max_length=255, verbose_name='Полное название')),
            ],
            options={
                'verbose_name': 'Категории меню',
                'verbose_name_plural': 'Категории меню',
            },
        ),
        migrations.CreateModel(
            name='TreeMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('path', models.CharField(blank=True, max_length=1000, verbose_name='Ссылка')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TreeMenuCategory', verbose_name='Категория')),
                ('parent', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='app.TreeMenu', verbose_name='Родительский элемент')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
