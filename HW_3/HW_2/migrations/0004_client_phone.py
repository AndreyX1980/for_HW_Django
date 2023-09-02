from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2', '0003_alter_client_reg_date_alter_product_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.IntegerField(default=None),
        ),
    ]