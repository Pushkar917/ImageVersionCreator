import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.uploader.models import OriginalImage
from apps.versionImage.models import PortFolioImageVesions, LandscapeImageVesions, LogoImageVersions
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Importing the StringIO module.
from io import StringIO,BytesIO



logger = logging.getLogger("__name__")

@receiver(post_save, sender=OriginalImage)
def create_oriimage_portfolio(sender, instance, created,**kwargs):
    if created:
        img_io = BytesIO()
        size = 300, 400
        original_image = Image.open(instance.image.path).convert('RGB')
        original_image.thumbnail(size, Image.Resampling.LANCZOS)
        if original_image.mode in ["RGBA", "P"]:
            original_image.convert("RGB")
            original_image.save(img_io, format='JPEG')
        else:
            original_image.save(img_io, format='JPEG')
        img_content = ContentFile(img_io.getvalue(), 'portfolio_'+ instance.title + '.jpg')
        PortFolioImageVesions.objects.create(portfolio_field=img_content,original_image=instance)


@receiver(post_save, sender=OriginalImage)
def save_image_portfolio(sender, instance, **kwargs):
 
    # here portfolio_image is related name for original image as foreign key
    instance.portfolio_image.save()
    logger.info("Portfolio image created")



@receiver(post_save, sender=OriginalImage)
def create_origimages_landscape(sender, instance, created,**kwargs):
    if created:
        img_io = BytesIO()
        size = 1600, 900
        original_image = Image.open(instance.image.path)
        original_image.thumbnail(size, Image.Resampling.LANCZOS)
        original_image.save(img_io, format='JPEG')
        img_content = ContentFile(img_io.getvalue(), 'landscape_'+ instance.title + '.jpg')
        LandscapeImageVesions.objects.create(landscape_field=img_content,original_image=instance)


@receiver(post_save, sender=OriginalImage)
def save_image_landscape(sender, instance, **kwargs):
 
    # here portfolio_image is related name for original image as foreign key
    instance.landscape_image.save()
    logger.info("Landscape image created")



@receiver(post_save, sender=OriginalImage)
def create_origimages_logo(sender, instance, created,**kwargs):
    if created:
        img_io = BytesIO()
        size = 100, 100
        original_image = Image.open(instance.image.path)
        original_image.thumbnail(size, Image.Resampling.LANCZOS)
        original_image.save(img_io, format='JPEG')
        img_content = ContentFile(img_io.getvalue(), 'logo_'+ instance.title + '.jpg')
        LogoImageVersions.objects.create(logo_field=img_content,original_image=instance)


@receiver(post_save, sender=OriginalImage)
def save_image_landscape(sender, instance, **kwargs):
 
    # here portfolio_image is related name for original image as foreign key
    instance.logo_image.save()
    logger.info("Landscape image created")








