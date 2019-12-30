from django.db import models
# USEER
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.utils.text import slugify
# Create your models here.

#-------- ETUDIANT --------#
class Profile(models.Model):
    """Model definition for Profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    contacts = models.CharField(max_length=30, null=True)
    genre = models.CharField(max_length=20, null=True)
    pays = models.CharField(max_length=255, null=True)
    ville = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    images = models.ImageField(upload_to='images/avatar/', default="photo.png")
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.user_profile.save()
    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username

#----------- JOURS -----------------#

 
class Jours(models.Model):
    jours = models.DateField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE, null=True,related_name= 'addby')
    debut_heure_arrivee = models.TimeField(null=True, default='08:00')
    fin_heure_arrivee = models.TimeField(null=True, default='10:00')
    titre_slug = models.SlugField(max_length=255,editable=False,null=True,unique=True)
    status =  models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str( self.jours)
    
    def save(self, *args, **kwargs):
            
        super(Jours, self).save(*args, **kwargs)
        self.titre_slug = slugify(self.created_at+str(self.id))
        super(Jours, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Exercice."""

        verbose_name = 'Jours'
        verbose_name_plural = 'Jours'
        ordering = ('created_at',)

class Presence(models.Model):
    
    etudiant = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True, related_name='userpresence')
    jours = models.ForeignKey(Jours, on_delete=models.CASCADE, related_name='joursap')
    heure_arrivee = models.TimeField(null=True)
    heure_depart = models.TimeField(null=True, default='17:00')
    status = models.BooleanField(default=False)
    status =  models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        unique_together = ('etudiant', 'jours',)

    