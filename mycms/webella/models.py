from django.db import models
from accounts.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.    

class user_dashboard(models.Model):
    WEBSITE_TYPES = (
    ('B','BLOG'), 
    ('P', 'PORTFOLIO'),
    
    )
   
    template_style = models.CharField(max_length=200)
    website_type = models.CharField(max_length=50, choices=WEBSITE_TYPES, default='B')
    
    user = models.ForeignKey("accounts.User", verbose_name=_("owner of website"), on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.user.email
    