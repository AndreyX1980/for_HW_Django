from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2', '0005_rename_name_product_title_alter_client_reg_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateField(),
        ),
    ]