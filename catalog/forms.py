from django import forms
from django.forms import ModelForm, IntegerField, Textarea
from .models import Yeast, Media, StorageInstance
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking inoculated date is after created.

class CreateStorageInstanceForm(forms.ModelForm):
    """
    Form for creating new storage instances
    """
    #Form variables
    storageinstance_count = IntegerField(label='Number of storage items created',help_text='Must be an integer greater than zero',min_value=1) 

    def clean_storageinstance_count(self):
        data = self.cleaned_data['storageinstance_count']

        #Check if count if >=1
        if data < 1:
            raise ValidationError(_('Number of storage instances must be 1 or more'))

        return data

    class Meta:
        model = StorageInstance
        fields = '__all__'
        exclude = ('parent','date_inoculated',)

class YeastForm(forms.ModelForm):
    model = Yeast
    fields = '__all__'
    widgets = {
        'comments': Textarea(attrs={'cols': 80, 'rows': 20})
    }
