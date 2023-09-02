from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2', '0006_alter_product_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateField(auto_now_add=True),
        ),
    ]