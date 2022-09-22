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
        fields = "__all__"
        widgets = {
            'vehicle_number': forms.widgets.TextInput(attrs={'data-inputmask': "'mask': 'AA-99-AA-9999'"}),
            'purchase_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
### Driver Forms ###
class DriverCreateForm(BSModalModelForm):
    class Meta:
        model = Driver
        fields = "__all__"
        widgets = {
            'contact': forms.widgets.TextInput(attrs={'data-inputmask': "'mask': '9999999999'"})
        }
        
### Route Forms ###
class RouteCreateForm(BSModalModelForm):
    class Meta:
        model = Route
        fields = "__all__"