from django.test import TestCase
from django.db import models
from catalog.models import Yeast, StorageInstance, Media
import datetime

# Create your tests here.

class YeastModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_yeast = Yeast.objects.create(
            name = "Test yeast", 
            yeast_type = "Test type",
            comments = "Test comments",
            attenuation = 10,
            upper_temp = 25,
            lower_temp = 20,
            flocculation = "Low",
            character = "Clean",
            tolerance = 15,                 
        )
        
        test_media = Media.objects.create(
            name = "Test media",
            date_created = datetime.date(2018, 1, 1),
            media_type = "Agar",
            volume = 500,
            gravity = 1045,
            comments = "Test media comments",
        )

        test_storage = StorageInstance.objects.create(
            yeast = test_yeast,
            date_created = datetime.date(2018, 1, 1),
            date_inoculated = datetime.date(2018, 2, 2),
            storage_type = "Slant",
            media = test_media,
            storage_status = "Inoculated",
            comments = "Test storage comment", 
        )
        pass

    #Yeast model attributes tests - maybe group these in a class?
    def test_name_type(self):
        self.assertIsInstance(Yeast.objects.get(id=1)._meta.get_field('name'),models.CharField)

    def test_name_label(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('name').verbose_name,'name')

    def test_name_max_length(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('name').max_length,100)

    def test_yeast_type_type(self):
        self.assertIsInstance(Yeast.objects.get(id=1)._meta.get_field('yeast_type'),models.CharField)

    def test_yeast_type_label(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('yeast_type').verbose_name,'yeast type')

    def test_yeast_type_max_length(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('yeast_type').max_length,10)

    def test_comments_type(self):
        self.assertIsInstance(Yeast.objects.get(id=1)._meta.get_field('comments'),models.CharField)

    def test_comments_label(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('comments').verbose_name,'comments')
    
    def test_comments_max_length(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('comments').max_length,255)

    def test_attenuation_type(self):
        self.assertIsInstance(Yeast.objects.get(id=1)._meta.get_field('attenuation'),models.PositiveSmallIntegerField)

    def test_attenuation_label(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('attenuation').verbose_name,'attenuation')
    
    def test_upper_temp_type(self):
        self.assertIsInstance(Yeast.objects.get(id=1)._meta.get_field('upper_temp'),models.PositiveSmallIntegerField)

    def test_upper_temp_label(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('upper_temp').verbose_name,'upper temp')
    
    def test_lower_temp_type(self):
        self.assertIsInstance(Yeast.objects.get(id=1)._meta.get_field('lower_temp'),models.PositiveSmallIntegerField)

    def test_lower_temp_label(self):
        self.assertEquals(Yeast.objects.get(id=1)._meta.get_field('lower_temp').verbose_name,'lower temp')
    
    #Yeast model methods tests

    def test_str_self(self):
        self.assertEquals(Yeast.objects.get(id=1).__str__(),"Test yeast (Test type)")