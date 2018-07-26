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

class UpdateStorageInstanceForm(forms.ModelForm):
    """
    Form for updating an existing storage instance
    """
    #Remove self from foreign key list to prevent referencing self as a parent
    #Need to limit query set to only storage instances with the same yeast strain
    #JS in the browser is the best way to do this - pass the complete dropdown list to the broswer (code below works fine)_
    #Then filter the list dynamically when the user selects an item from the "Yeast" listbox on the form to_
    #filter the listbox source list based on the selected "Yeast"
    def __init__(self, *args, **kwargs):
            super(UpdateStorageInstanceForm, self).__init__(*args, **kwargs)
            self.fields['parent'].queryset = StorageInstance.objects.exclude(id__exact=self.instance.id)
    
    class Meta:
        model = StorageInstance
        fields = '__all__'
