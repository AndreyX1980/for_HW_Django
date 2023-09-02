from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw_2', '0004_client_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='client',
            name='reg_date',
            field=models.DateField(),
        ),
    ]