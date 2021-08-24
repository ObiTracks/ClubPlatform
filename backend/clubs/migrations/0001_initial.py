# Generated by Django 3.1.5 on 2021-08-22 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=60)),
                ('who_are_we', models.TextField(blank=True, max_length=1000)),
                ('mission_statement', models.TextField(blank=True, max_length=1000)),
                ('vision', models.TextField(blank=True, max_length=1000)),
                ('objectives', models.TextField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('history', models.TextField(blank=True, max_length=1000)),
                ('discord_link', models.CharField(blank=True, max_length=1000)),
                ('slack_link', models.CharField(blank=True, max_length=1000)),
                ('facebook_link', models.CharField(blank=True, max_length=1000)),
                ('instagram_link', models.CharField(blank=True, max_length=1000)),
                ('twitter_link', models.CharField(blank=True, max_length=1000)),
                ('linkedin_link', models.CharField(blank=True, max_length=1000)),
                ('shared_calendar_link', models.CharField(blank=True, max_length=1000)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('short_description', models.TextField(max_length=1000)),
                ('long_description', models.TextField(blank=True, max_length=1000)),
                ('location', models.CharField(choices=[('HB', 'Hybrid'), ('IP', 'In-Person'), ('R', 'Remote')], default='R', max_length=100)),
                ('physical_location', models.CharField(blank=True, max_length=100)),
                ('url', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('year_level', models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', 'Fourth'), ('5', 'Fifth'), ('NA', 'Not Applicable')], default='M', max_length=40)),
                ('role', models.CharField(choices=[('M', 'Member'), ('TL', 'Team Lead'), ('E', 'Executive'), ('VP', 'Vice President'), ('P', 'President')], default='M', max_length=40)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('clubs', models.ManyToManyField(blank=True, default=None, to='clubs.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('community_drive_url', models.CharField(blank=True, max_length=100)),
                ('repo_url', models.CharField(blank=True, max_length=100)),
                ('external_url', models.CharField(blank=True, max_length=100)),
                ('pod_lead', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.member')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=60)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('time', models.DateTimeField()),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(blank=True, max_length=100)),
                ('external_url', models.CharField(max_length=1000)),
                ('priority_level', models.CharField(blank=True, choices=[('H', 'High'), ('R', 'Regular')], default='R', max_length=150)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.member')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.event')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('time', models.DateTimeField()),
                ('url', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('resource_type', models.CharField(blank=True, choices=[('G', 'Community Game'), ('LV', 'Learning Video'), ('LD', 'Learning Document'), ('D', 'Documentation'), ('U', 'Useful Resource'), ('S', 'School Resource')], max_length=150)),
                ('club', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.club')),
                ('pod', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.pod')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.CharField(blank=True, max_length=100)),
                ('time', models.DateTimeField()),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, choices=[('HB', 'Hybrid'), ('IP', 'In-Person'), ('R', 'Remote')], max_length=150)),
                ('url', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.member')),
                ('club', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.club')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clubs.school'),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clubs.member'),
        ),
        migrations.AddField(
            model_name='event',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.club'),
        ),
        migrations.AddField(
            model_name='club',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clubs.school'),
        ),
    ]
