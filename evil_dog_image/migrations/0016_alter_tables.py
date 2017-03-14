from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('evil_dog_image', '0015_drop_tables'),
    ]
    operations = [
        migrations.RunSQL("alter sequence inventory_charitydesign_id_seq rename to evil_dog_image_charitydesign_id_seq"),
        migrations.RunSQL("alter table inventory_graphicdesign rename to evil_dog_image_graphicdesign"),
        migrations.RunSQL("alter sequence inventory_graphicdesign_id_seq rename to evil_dog_image_graphicdesign_id_seq"),
        migrations.RunSQL("alter sequence inventory_item_id_seq rename to evil_dog_image_item_id_seq"),
        migrations.RunSQL("alter table inventory_likes rename to evil_dog_image_likes"),
        migrations.RunSQL("alter sequence inventory_likes_id_seq rename to evil_dog_image_likes_id_seq"),
        migrations.RunSQL("alter table inventory_paintings rename to evil_dog_image_paintings")

    ]
