from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='phone',
        ),
    ]