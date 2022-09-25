from django import forms
from .models import Customer, Destination, Driver, Vehicle, Wheel, Route, VehicleMaintenance, Trip, Fuel
from bootstrap_modal_forms.forms import BSModalModelForm


### Customer Forms ###
class CustomerCreateForm(BSModalModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

### Destination Forms ###
class DestinationCreateForm(BSModalModelForm):
    class Meta:
        model = Destination
        fields = "__all__"
    
### Vehicle Forms ###
class VehicleCreateForm(BSModalModelForm):
    class Meta:
        model = Vehicle
        exclude = ('available',)
        widgets = {
            'vehicle_number': forms.widgets.TextInput(attrs={'data-inputmask': "'mask': 'AA-99-AA-9999'"}),
            'purchase_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
### Driver Forms ###
class DriverCreateForm(BSModalModelForm):
    class Meta:
        model = Driver
        exclude = ('available',)
        widgets = {
            'contact': forms.widgets.TextInput(attrs={'data-inputmask': "'mask': '9999999999'"})
        }
        
### Route Forms ###
class RouteCreateForm(BSModalModelForm):
    class Meta:
        model = Route
        fields = "__all__"

### Trip Forms ###
class TripCreateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(TripCreateForm, self).__init__(*args, **kwargs)
        self.fields['driver'].queryset = Driver.objects.all()
        self.fields['vehicle_number'].queryset = Vehicle.objects.all()
        
        instance = getattr(self, 'instance', None)
        
        if instance and instance.pk:
            self.fields['trip_id'].disabled = True
    class Meta:
        model = Trip
        exclude = ('message_id', 'complete', 'end_date')
        widgets = {
            'trip_id': forms.widgets.TextInput(attrs={'disabled': 'disabled'}),
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'product': forms.widgets.TextInput(attrs={'class': 'AutoComplete typeahead tt-query', 'autocomplete': 'off'}),
        }
        