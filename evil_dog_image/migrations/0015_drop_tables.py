from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('evil_dog_image', '0014_likes_user_profile'),
    ]
    operations = [
        migrations.RunSQL("drop sequence evil_dog_image_charitydesign_id_seq cascade"),
        migrations.RunSQL("drop table evil_dog_image_charitydesign cascade"),
        migrations.RunSQL("drop sequence evil_dog_image_graphicdesign_id_seq cascade"),
        migrations.RunSQL("drop table evil_dog_image_graphicdesign cascade"),
        migrations.RunSQL("drop sequence evil_dog_image_paintings_id_seq cascade"),
        migrations.RunSQL("drop table evil_dog_image_paintings cascade"),
        migrations.RunSQL("drop sequence evil_dog_image_item_id_seq cascade"),
        migrations.RunSQL("drop sequence evil_dog_image_likes_id_seq cascade"),
        migrations.RunSQL("drop table evil_dog_image_likes cascade"),
    ]
