# Generated by Django 2.0 on 2017-12-03 02:27

from django.db import migrations, models
import django.db.models.deletion
import djstripe.models
import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0013_remove_card_stripe_id_default'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebhookEventTrigger',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('remote_ip', models.GenericIPAddressField(help_text='IP address of the request client.')),
                ('headers', djstripe.fields.JSONField()),
                ('body', models.TextField(blank=True)),
                ('valid', models.BooleanField(default=False, help_text='Whether or not the webhook event has passed validation')),
                ('processed', models.BooleanField(default=False, help_text='Whether or not the webhook event has been successfully processed')),
                ('exception', models.CharField(blank=True, max_length=128)),
                ('traceback', models.TextField(blank=True, help_text='Traceback if an exception was thrown during processing')),
                ('djstripe_version', models.CharField(default=djstripe.models._get_version, help_text='The version of dj-stripe when the webhook was received', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='eventprocessingexception',
            name='event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='received_api_version',
            new_name='api_version',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='webhook_message',
            new_name='data',
        ),
        migrations.RemoveField(
            model_name='event',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='event',
            name='processed',
        ),
        migrations.RemoveField(
            model_name='event',
            name='valid',
        ),
        migrations.DeleteModel(
            name='EventProcessingException',
        ),
        migrations.AddField(
            model_name='webhookeventtrigger',
            name='event',
            field=models.ForeignKey(blank=True, help_text='Event object contained in the (valid) Webhook', null=True, on_delete=django.db.models.deletion.SET_NULL, to='djstripe.Event'),
        ),
    ]
