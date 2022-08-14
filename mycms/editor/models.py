from django.db import models
from accounts.models import User

from django.utils.translation import gettext_lazy as _

# Create your models here.

class hannahTemplate(models.Model):

    nav_text1 = models.CharField(_("nav text 1"), max_length=50, default="Home")
    nav_text2 = models.CharField(_("nav text 2"), max_length=50, default="Resume")
    nav_text3 = models.CharField(_("nav text 3"), max_length=50, default="Contact")
    page_title = models.CharField(_("page title"), max_length=50, default="Product Designer")
    
    #hero-image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    
    hero_text_small = models.CharField(_("hero small text"), max_length=50, default="Hi there!")
    hero_text_big = models.CharField(_("hero big text"), max_length=50, default="I am Hannah James")
    
    background_color = models.CharField(_("background color"), max_length=50, default="#f4e0e0")
    hero_div_color = models.CharField(_("landing page color"), max_length=50, default="#fcbbbb")
    
    user = models.ForeignKey("accounts.User", verbose_name=_("owner of website"), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.email

