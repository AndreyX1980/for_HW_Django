from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2', '0002_remove_client_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='reg_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]