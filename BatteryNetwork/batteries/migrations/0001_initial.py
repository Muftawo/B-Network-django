# Generated by Django 4.0.6 on 2022-07-07 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('battery_code', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cell_type', models.CharField(choices=[('NMC', 'Nickel Manganese Cobalt'),
                                                        ('LFP', 'Lithium Iron Phosphate')], max_length=5)),
                ('batch_num', models.IntegerField()),
                ('soc', models.FloatField()),
                ('soh', models.FloatField()),
                ('latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('iot_live', models.BooleanField()),
            ],
        ),
    ]