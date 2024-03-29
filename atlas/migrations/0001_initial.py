# Generated by Django 2.1.1 on 2018-10-01 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('builder_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('city_region', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, verbose_name='Name of Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('imo', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='IMO Number')),
                ('call_sign', models.CharField(blank=True, max_length=200, verbose_name='Call Sign')),
                ('year_built', models.PositiveSmallIntegerField(verbose_name='Year Built')),
                ('length', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Length (m)')),
                ('beam', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Beam (m)')),
                ('tonnage', models.PositiveIntegerField(blank=True, null=True, verbose_name='Gross Tonnage')),
                ('website', models.URLField(blank=True, verbose_name='Website')),
                ('former_names', models.TextField(blank=True, verbose_name='Former Names')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('builder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Builder', verbose_name='Builder')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.City', verbose_name='Location - City')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Country', verbose_name='Location - Country')),
                ('flag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Flag', verbose_name='Flag')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Owner', verbose_name='Owner')),
                ('register', models.ManyToManyField(blank=True, to='atlas.Register', verbose_name='Historic Register(s)')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ship',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Status', verbose_name='Current Status'),
        ),
        migrations.AddField(
            model_name='ship',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Type', verbose_name='Type of Ship'),
        ),
        migrations.AddField(
            model_name='ship',
            name='use',
            field=models.ManyToManyField(to='atlas.Use', verbose_name='Current Use(s)'),
        ),
        migrations.AddField(
            model_name='builder',
            name='builder_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.City'),
        ),
        migrations.AddField(
            model_name='builder',
            name='builder_country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='atlas.Country'),
        ),
    ]
