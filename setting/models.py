from django.db import models

# Create your models here.
class Settings(models.Model):
    logo         = models.ImageField(upload_to='settings/')
    description    = models.TextField(max_length=2000)
    phone          = models.CharField(max_length=50)
    email          = models.EmailField( max_length=254)
    address        = models.CharField(max_length=50)
    site_name      = models.CharField(max_length=50)
    tw_link        = models.URLField( max_length=200)
    fb_link        = models.URLField( max_length=200)
    inst_link      = models.URLField( max_length=200)
    

    def __str__(self):
        return self.name


