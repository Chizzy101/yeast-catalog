from django.core import serializers
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# import sys for debugging - saving JSON serialise
import sys

# Create your models here.

class Yeast(models.Model):
    """
    Model representing a yeast strain in the catalog
    """

    name = models.CharField(max_length=100, help_text="Enter the name of the yeast strain")

    TYPE_LIST = (
        ("Ale", "Ale"),
        ("Lager", "Lager"),
        ("Cider","Cider"),
        ("Champagne","Champagne"),
        ("Wine","Wine"),
    )

    yeast_type = models.CharField(max_length=10, choices=TYPE_LIST, blank=True, help_text='Yeast type')
    comments = models.CharField(max_length=255, help_text="Enter comments (up to 255 characters)")
    attenuation = models.PositiveSmallIntegerField(null=True)
    # Need to add logic to check upper temp is higer than lower temp when either is provided. Do this in form
    upper_temp = models.PositiveSmallIntegerField(null=True)
    lower_temp = models.PositiveSmallIntegerField(null=True)
    
    FLOC_LIST = (
        ('L', 'Low'),
        ('M', 'Moderate'),
        ('H', 'High'),
    )

    flocculation = models.CharField(max_length=1, choices=FLOC_LIST, blank=True, help_text='Yeast flocculation')
    # This logic should be used in a dynamic list box, with list options based on yeast_type selected - do in form
    CHARACTER_LIST = (
        ('Clean','Clean'),
        ('Fruity','Fruity'),
        ('Hybrid','Hybrid'),
        ('Phenolic','Phenolic'),
        ('Eccentric','Eccetric'),
        ('Dry','Dry'),
        ('Full','Full'),
    )
    
    character = models.CharField(max_length=10, choices=CHARACTER_LIST, blank=True, help_text='Yeast category')
    tolerance = models.PositiveSmallIntegerField(null=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '{0} ({1})'.format(self.name,self.yeast_type)

    def get_absolute_url(self):
        """
        Returns the url to access a particular yeast instance
        """
        return reverse('yeast-detail', args=[str(self.id)])

    def get_yeast_count(self):
        """
        Returns the count of storage instances available with the yeast strain
        """
        available_yeast_count = self.storageinstance_set.filter(storage_status='i').count()
        return available_yeast_count
    
    def get_inoculated_list(self):
        """
        Returns a list of available storage instances inoculated with a yeast
        """
        inoculated_storage_list = self.storageinstance_set.filter(storage_status='i')
        return inoculated_storage_list

    def get_used_list(self):
        """
        Returns a list of used storage instances inoculated with a yeast 
        """
        used_storage_list = self.storageinstance_set.filter(storage_status='u')
        return used_storage_list

class Media(models.Model):
    """
    Model representing the types of growth media yeast can be grown and stored on
    """

    name = models.CharField(max_length=100, help_text='Enter the name for the media')
    date_created = models.DateField(null=True, blank=True)

    MEDIA_TYPE = (
        ('a','Agar'),
        ('w','Wort'),
        ('g','Glycerin'),
        ('sc','Sodium chloride'),
        ('g','Gelatine'),
    )

    media_type = models.CharField(max_length=100,choices=MEDIA_TYPE, help_text='Select the appropriate media type')
    volume = models.PositiveSmallIntegerField(null=True, help_text="Enter the total volume of media created")
    gravity = models.PositiveSmallIntegerField(null=True, help_text="Enter the gravity of media created")
    comments = models.CharField(max_length=255, help_text="Enter comments (up to 255 characters)")

    class Meta:
        ordering = ['date_created']
        verbose_name_plural = 'Media'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return '{0} ({1}) - {2}'.format(self.name,self.get_media_type_display(),self.date_created)

    def get_absolute_url(self):
        """
        Returns the url to access a particular media.
        """
        return reverse('media-detail', args=[str(self.id)])

    def get_inoculated_list(self):
        """
        Returns a list of inoculated storage instances using a particular media.
        """
        inoculated_storage_list = self.storageinstance_set.filter(storage_status='i')
        return inoculated_storage_list

    def get_available_list(self):
        """
        Returns a list of available storage instances using a particular media.
        """
        available_storage_list = self.storageinstance_set.filter(storage_status='a')
        return available_storage_list

    def get_used_list(self):
        """
        Returns a list of used/discarded storage instances using a particular media.
        """
        used_storage_list = self.storageinstance_set.filter(storage_status='u')
        return used_storage_list

class StorageInstance(models.Model):
    """
    Model representing each instance of storage in the catalog
    """

    yeast = models.ForeignKey('Yeast', on_delete=models.SET_NULL, blank=True, null=True)
    # need to put some logic here that a storage instance can't have itself as a parent
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    date_created = models.DateField(null=True)
    date_inoculated = models.DateField(null=True, blank=True)

    STORAGE_TYPE_LIST = (
        ('s','Slant'),
        ('p','Plate'),
        ('sol','Solution'),
        ('f','Freeze'),
        ('o','Other'),
    )

    storage_type = models.CharField(max_length=100,choices=STORAGE_TYPE_LIST, help_text='Select the appropriate yeast storage category')
    media = models.ForeignKey('Media', on_delete=models.SET_NULL, null=True)

    STORAGE_STATUS_LIST = (
        ('u','Used / Discarded'),
        ('i','Inoculated'),
        ('a','Available'),
    )
    
    storage_status = models.CharField(max_length=100,choices=STORAGE_STATUS_LIST, help_text='Select the appropriate media type')
    comments = models.CharField(max_length=255, help_text="Enter comments (up to 255 characters)")

    class Meta:
        ordering = ['id']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # might add some more logic here - if inoculated, then pass yeast type and date inoculated in return else return the string below
        return '{0} ({1}) - {2}'.format(self.id, self.get_storage_type_display(), self.get_storage_status_display())
    
    #Need to write a method that generates a queryset with related storage instances and serialises the queryset_
    # to a JSON object. This object can then be passed to the browser to render the tree diagram showing the yeast's lineage_
    # Note this only needs to cover inoculated yeasts
    def create_JSON_relatives(self):
        #create the queryset to serialises 
        # move this into serialise statement once confirmed working
        relative_set = StorageInstance.objects.filter(yeast=self.yeast)
        #serialise statement
        serial_data = serializers.serialize('json', relative_set, fields=('id','parent'))
        print(serial_data)
        f = open("out.json",'w')
        f.write(serial_data)
        f.close

    def get_absolute_url(self):
        """
        Returns the url to access a particular storage instance.
        """
        return reverse('storageinstance-detail', args=[str(self.id)])