from django.db import models
import datetime
import os
from django.utils.text import slugify
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
        return f"{self.unique_id}"


    def save(self, *args, **kwargs):
        # 1 Générer un unique_id si vide
        if not self.unique_id:
            self.unique_id = datetime.datetime.strftime(self.created_At,f"%H_%M_%S_{self.label}") # ID unique automatique
        
        self.file.name = self.file.name.replace(" ","_")

        print(
            f"""
            {self.file.name}
        """
        )


        # 2 Renommer le fichier uploadé (si un fichier est fourni)
        # if self.file and not self.file.name.startswith("inputs/"):
        #     ext = os.path.splitext(self.file.name)[1]  # extension (.pdf, .png, etc.)
        #     new_name = f"inputs/{self.unique_id}{ext}"
        #     self.file.name = new_name
        # 3 Appeler la méthode parent pour sauvegarder
        super().save(*args, **kwargs)






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




