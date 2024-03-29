# Generated by Django 4.2.8 on 2023-12-21 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objeto', '0001_initial'),
        ('arma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalarma',
            name='objeto',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='objeto.objeto', verbose_name='Objeto'),
        ),
        migrations.AddField(
            model_name='arma',
            name='objeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='armas', to='objeto.objeto', verbose_name='Objeto'),
        ),
    ]
