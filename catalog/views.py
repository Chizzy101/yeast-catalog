from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy
from .models import Yeast, Media, StorageInstance
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from .forms import CreateStorageInstanceForm
import datetime #to set initial value of date field to today

# Create your views here.

def index(request):
    """
    View function for home page of application.
    """
    # Generate counts of some of the main objects
    num_yeast=Yeast.objects.all().count()
    num_instances=StorageInstance.objects.all().count()
    # Available yeast (status = 'a')
    num_instances_available=StorageInstance.objects.filter(storage_status__exact='i').count()
    num_media=Media.objects.all().count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_yeast':num_yeast,'num_instances':num_instances, 'num_media':num_media, 'num_instances_available':num_instances_available},
    )

class YeastListView(generic.ListView):
    model = Yeast

class YeastDetailView(generic.DetailView):
    model = Yeast

class YeastCreate(PermissionRequiredMixin, CreateView):
    model = Yeast
    fields = '__all__'
    permission_required = 'catalog.is_staff'

class YeastUpdate(PermissionRequiredMixin, UpdateView):
    model = Yeast
    fields = '__all__'
    permission_required = 'catalog.is_staff'

class YeastDelete(PermissionRequiredMixin, DeleteView):
    model = Yeast
    success_url = reverse_lazy('yeasts')
    permission_required = 'catalog.is_staff'

def storageList(request):
    """
    View function for storage instance list
    """
    list_storage_inoculated=StorageInstance.objects.filter(storage_status__exact='i')
    list_storage_available=StorageInstance.objects.filter(storage_status__exact='a')
    list_storage_used=StorageInstance.objects.filter(storage_status__exact='u')

    return render(
        request,
        'catalog/storageinstance_list.html',
        context={'list_storage_inoculated':list_storage_inoculated, 'list_storage_available':list_storage_available,'list_storage_used':list_storage_used},
    )

class StorageInstanceDetailView(generic.DetailView):
    model = StorageInstance

@login_required
@permission_required('catalog.can_add_storageinstance')
def create_storage_instance(request):
    """
    View function for creating storage instances
    """

    today = datetime.datetime.today().strftime('%Y-%m-%d')
    create_list = []

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CreateStorageInstanceForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            create_list = [StorageInstance(
                date_created=form.cleaned_data['date_created'],
                storage_type=form.cleaned_data['storage_type'],
                media=form.cleaned_data['media'],
                storage_status=form.cleaned_data['storage_status'],
                comments=form.cleaned_data['comments'],
                )
                for i in list(range(0,form.cleaned_data['storageinstance_count']))]
            # bulk create of StorageInstance objects based on counter from form
            StorageInstance.objects.bulk_create(create_list)
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('storage'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = CreateStorageInstanceForm(initial={'date_created':today,'storage_status':'a','storageinstance_count':1})

    return render(request, 'catalog/storageinstance_create.html',{'form':form})

class StorageInstanceUpdate(PermissionRequiredMixin, UpdateView):
    model = StorageInstance
    fields = '__all__'
    permission_required = 'catalog.is_staff'

    
class StorageInstanceDelete(PermissionRequiredMixin, DeleteView):
    model = StorageInstance
    success_url = reverse_lazy('storage')
    permission_required = 'catalog.is_staff'
    
class MediaListView(generic.ListView):
    model = Media

class MediaDetailView(generic.DetailView):
    model = Media

class MediaCreate(PermissionRequiredMixin, CreateView):
    model = Media
    fields = '__all__'
    permission_required = 'catalog.is_staff'

class MediaUpdate(PermissionRequiredMixin, UpdateView):
    model = Media
    fields = '__all__'
    permission_required = 'catalog.is_staff'

class MediaDelete(PermissionRequiredMixin, DeleteView):
    model = Media
    success_url = reverse_lazy('media')
    permission_required = 'catalog.is_staff'

def testdocument(request):
    return render(
        request,
        'catalog/test_doc.html',
    )