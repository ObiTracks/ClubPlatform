# Generated by Django 3.1.5 on 2021-07-31 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('M', 'Member'), ('TL', 'Team Lead'), ('E', 'Executive'), ('VP', 'Vice President'), ('P', 'President')], default='M', max_length=40),
        ),
        migrations.AddField(
            model_name='member',
            name='year_level',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth')], default='M', max_length=40),
        ),
        migrations.AlterField(
            model_name='club',
            name='description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='club',
            name='history',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='club',
            name='mission_statement',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='club',
            name='objectives',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='club',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clubs.school'),
        ),
        migrations.AlterField(
            model_name='club',
            name='vision',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='club',
            name='who_are_we',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(choices=[('HB', 'Hybrid'), ('IP', 'In-Person'), ('R', 'Remote')], default='R', max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='long_description',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='clubs',
            field=models.ManyToManyField(blank=True, default=None, to='clubs.Club'),
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, choices=[('HB', 'Hybrid'), ('IP', 'In-Person'), ('R', 'Remote')], max_length=150),
        ),
    ]
