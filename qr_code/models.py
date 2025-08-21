from django.db import models
import datetime

# Create your models here.


class Document(models.Model):
    id    = models.IntegerField(
        unique=True,
        primary_key=1,
        null=False
    )
    
    label = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    
    created_At = models.DateTimeField(
        null=False,
        default=datetime.datetime.now
    )
    
    unique_id  = models.CharField(
        unique = True,
        max_length=255,
        blank=True,
        null=False,
        auto_created=""
    )
    file = models.FileField(
        upload_to="inputs/",
        default="inputs/input.pdf"
    )
    
    
    def __str__(self):
        return f"{self.label} ({self.unique_id})"





# the scan 
class Scan(models.Model):
    id = models.IntegerField(
        primary_key=True,
        blank=False,
    )

    label = models.CharField(
        max_length=255,
        blank=True,
        null=False,
        unique=True
    )

    document = models.ForeignKey(
        to=Document,
        on_delete= models.CASCADE
    )
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)




