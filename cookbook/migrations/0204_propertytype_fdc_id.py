# Generated by Django 4.2.7 on 2023-11-27 21:09

from django.db import migrations, models
from django_scopes import scopes_disabled


def fix_fdc_ids(apps, schema_editor):
    with scopes_disabled():
        # in case any food had a non digit fdc ID before this migration, remove it
        Food = apps.get_model('cookbook', 'Food')
        Food.objects.exclude(fdc_id__regex=r'^\d+$').exclude(fdc_id=None).update(fdc_id=None)


class Migration(migrations.Migration):
    dependencies = [
        ('cookbook', '0203_alter_unique_contstraints'),
    ]

    operations = [
        migrations.RunPython(fix_fdc_ids),
        migrations.AddField(
            model_name='propertytype',
            name='fdc_id',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]