from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import ProtectedError
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, View
from django.db.models import Q, Max, F
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalDeleteView
from logistics.models import *
from logistics.forms import *
from datetime import date


### Template Views for Login, Logout and Dashboard ###
class Login_Page(LoginView):
    template_name = 'login.html'
    
class Logout_Page(LogoutView):
    template_name = 'logout.html'    
    
class Dashboard_Page(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'
    
    
### Customer Views ###
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customer_list.html'    
    
class CustomerCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customer_create.html'    
    success_url = reverse_lazy('customer_list')
    success_message = "New Customer has been created successfully"

class CustomerUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customer_edit.html'    
    success_url = reverse_lazy('customer_list')
    success_message = "Customer has been edited successfully"
    
class CustomerDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    error_template = 'customer_list.html'
    success_url = reverse_lazy('customer_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Customer has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('customer_list')
        
        
### Destination Views ###
class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination
    template_name = 'destination_list.html'    
    
class DestinationCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Destination
    form_class = DestinationCreateForm
    template_name = 'destination_create.html'    
    success_url = reverse_lazy('destination_list')
    success_message = "New Destination has been created successfully"

class DestinationUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Destination
    form_class = DestinationCreateForm
    template_name = 'destination_edit.html'    
    success_url = reverse_lazy('destination_list')
    success_message = "Destination has been edited successfully"
    
class DestinationDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Destination
    template_name = 'destination_delete.html'
    error_template = 'destination_list.html'
    success_url = reverse_lazy('destination_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Destination has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('destination_list')
        
        
### Vehicle Views ###
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'    
    
class VehicleCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    template_name = 'vehicle_create.html'    
    success_url = reverse_lazy('vehicle_list')
    success_message = "New Vehicle has been created successfully"

class VehicleUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Vehicle
    form_class = VehicleCreateForm
    template_name = 'vehicle_edit.html'    
    success_url = reverse_lazy('vehicle_list')
    success_message = "Vehicle has been edited successfully"
    
class VehicleDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'
    error_template = 'vehicle_list.html'
    success_url = reverse_lazy('vehicle_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Vehicle has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('vehicle_list')
                
                
### Driver Views ###
class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    template_name = 'driver_list.html'    
    
class DriverCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Driver
    form_class = DriverCreateForm
    template_name = 'driver_create.html'    
    success_url = reverse_lazy('driver_list')
    success_message = "New Driver has been created successfully"

class DriverUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Driver
    form_class = DriverCreateForm
    template_name = 'driver_edit.html'    
    success_url = reverse_lazy('driver_list')
    success_message = "Driver has been edited successfully"
    
class DriverDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Driver
    template_name = 'driver_delete.html'
    error_template = 'driver_list.html'
    success_url = reverse_lazy('driver_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Driver has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('driver_list')


### Route Views ###
class RouteListView(LoginRequiredMixin, ListView):
    model = Route
    template_name = 'route_list.html'    
    
class RouteCreateView(LoginRequiredMixin, BSModalCreateView):
    model = Route
    form_class = RouteCreateForm
    template_name = 'route_create.html'    
    success_url = reverse_lazy('route_list')
    success_message = "New Route has been created successfully"

class RouteUpdateView(LoginRequiredMixin, BSModalUpdateView):
    model = Route
    form_class = RouteCreateForm
    template_name = 'route_edit.html'    
    success_url = reverse_lazy('route_list')
    success_message = "Route has been edited successfully"
    
class RouteDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Route
    template_name = 'route_delete.html'
    error_template = 'route_list.html'
    success_url = reverse_lazy('route_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Route has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('route_list')


### Trip Views ###
class OngoingTripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'trip_ongoing_list.html'
    
    def get_queryset(self):
        return self.model.objects.filter(complete=False)
    
class CompletedTripListView(LoginRequiredMixin, ListView):
    model = Trip
    template_name = 'trip_completed_list.html'
    
    def get_queryset(self):
        return self.model.objects.filter(complete=True)
    
class TripCreateView(LoginRequiredMixin, CreateView):
    model = Trip
    template_name = 'trip_create.html'
    form_class = TripCreateForm
    success_url = reverse_lazy('ongoing_trip_list')
    success_message = "New Trip has been logged successfully"

@login_required    
def get_product_listing(request):
    qs = list(Trip.objects.values_list('product',flat=True))
    return JsonResponse(qs, safe = False)    
    
class TripUpdateView(LoginRequiredMixin, UpdateView):
    model = Trip
    template_name = 'trip_edit.html'
    form_class = TripCreateForm
    success_url = reverse_lazy('ongoing_trip_list')
    success_message = "Trip has been edited successfully"    
    
class TripDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Trip
    template_name = 'trip_delete.html'
    error_template = 'ongoing_trip_list.html'
    success_url = reverse_lazy('ongoing_trip_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Trip has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('ongoing_trip_list')

class TripDetailView(LoginRequiredMixin, DetailView):
    model = Trip
    template_name = 'trip_detail.html'
    
@login_required
def TripPendingListView(request):
    queryset = Trip.objects.filter(complete = False) 
    return render(request,'trip_complete.html', {'data':queryset})           
    
class TripCloseView(SuccessMessageMixin, LoginRequiredMixin, View):    
    def post(self, request, *args, **kwargs):
        trips = self.request.POST.getlist('trips')
        dates = [i for i in self.request.POST.getlist('dates') if i]
                
        if len(trips) > 0:
            if len(trips) == len(dates):
                trip_list = Trip.objects.filter(pk__in = trips)
                for trip in trip_list:
                    identifier = set([str(trip.id)])
                    id_index = [i for i, e in enumerate(trips) if e in identifier][0]
                    end_date = dates[id_index]
                    if trip.start_date > datetime.strptime(end_date,"%Y-%m-%d").date():
                        messages.error(self.request, "Error! Trip End Date cannot be earlier than Trip Start Date", extra_tags='danger')
                        return redirect('trip_pending')
                    else:    
                        trip.complete = True
                        trip.end_date = end_date
                        
                        # Get Kms Travelled by Route
                        run_kms = trip.route.distance
                        wheels = Wheel.objects.filter(~Q(serial_number=None), vehicle_number=trip.vehicle_number, purchase_date__lte=trip.start_date)
                        if wheels.exists():
                            for wheel in wheels:
                                wheel.usage = F('usage') + run_kms
                                
                            Wheel.objects.bulk_update(wheels, ['usage'])
                        
            else:
                messages.error(self.request, "Error! If a Trip is completed, End Date should be mentioned", extra_tags='danger')
                return redirect('trip_pending')
            
                
            Trip.objects.bulk_update(trip_list, ['end_date','complete'])
            messages.success(self.request, "Selected Vehicle Trips Completed Successfully", extra_tags='success')
            
        return redirect('ongoing_trip_list')   
    
@login_required
def get_available_vehicles(request):
    chosen_date = datetime.strptime(request.GET.get('chosen_date'),"%Y-%m-%d").date()
    # Filter Trip Dataset #
    trip_qs = Trip.objects.all()
    ongoing_trip_id = trip_qs.filter(end_date = None)
    ongoing_trip_vehicles = ongoing_trip_id.values('vehicle_number')
    ongoing_trip_drivers = ongoing_trip_id.values('driver')
    completed_trip_id = trip_qs.exclude(id__in = ongoing_trip_id)
    completed_trip_vehicles_exclude = completed_trip_id.filter(start_date__lte = chosen_date, end_date__gte = chosen_date).values('vehicle_number')
    completed_trip_drivers_exclude = completed_trip_id.filter(start_date__lte = chosen_date, end_date__gte = chosen_date).values('driver')
    
    # Filter Available Vehicles #
    available_vehicles = list(Vehicle.objects.exclude(Q(id__in = ongoing_trip_vehicles) | Q(id__in = completed_trip_vehicles_exclude)).values_list('id','vehicle_number'))
    available_drivers = list(Driver.objects.exclude(Q(id__in = ongoing_trip_drivers) | Q(id__in = completed_trip_drivers_exclude)).values_list('id','full_name'))
    return JsonResponse(data={
        'available_vehicles': available_vehicles,
        'available_drivers': available_drivers,
        })
    

### Fuel Views ###

class FuelListView(LoginRequiredMixin, ListView):
    model = Fuel
    template_name = 'fuel_list.html'    
    
class FuelCreateView(LoginRequiredMixin, CreateView):
    model = Fuel
    form_class = FuelCreateForm
    template_name = 'fuel_create.html'    
    success_url = reverse_lazy('fuel_list')
    success_message = "Fuel Bill has been recorded successfully"

class FuelUpdateView(LoginRequiredMixin, UpdateView):
    model = Fuel
    form_class = FuelCreateForm
    template_name = 'fuel_edit.html'    
    success_url = reverse_lazy('fuel_list')
    success_message = "Fuel Bill has been edited successfully"
    
class FuelDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = Fuel
    template_name = 'fuel_delete.html'
    error_template = 'fuel_list.html'
    success_url = reverse_lazy('fuel_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Fuel Bill has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('fuel_list')

@login_required    
def get_station_listing(request):
    qs = list(Fuel.objects.values_list('station',flat=True).distinct())
    return JsonResponse(qs, safe = False)    
        
        
### Wheel Views ###

class WheelListView(LoginRequiredMixin, ListView):
    model = Wheel
        
    def get_queryset(self):
        return self.model.objects.filter(vehicle_number=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super(WheelListView, self).get_context_data(**kwargs)
        context['vehicle_number'] = Vehicle.objects.get(pk=self.kwargs['pk'])
        return context
        
class WheelCreateView(LoginRequiredMixin, CreateView):    
    model = Wheel
    template_name = 'wheel_create.html'
    form_class = WheelCreateForm
    
    def dispatch(self, request, *args, **kwargs):
        self.vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        return super(WheelCreateView, self).dispatch(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(WheelCreateView, self).get_context_data(**kwargs)
        context['wheels_form'] = forms.modelformset_factory(Wheel, WheelCreateForm, 
                                      fields=['serial_number','purchase_date','running_life'], 
                                      extra = self.vehicle.axle, can_delete = False)(queryset=Wheel.objects.none())
        context['vehicle_number'] = self.vehicle
        return context
    
    def post(self, request, *args, **kwargs):
        formset = forms.modelformset_factory(Wheel, WheelCreateForm, 
                                      fields=['serial_number','purchase_date','running_life'], 
                                      can_delete = False)(request.POST or None)
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            return render(request, 'wheel_create.html', {'wheels_form' : formset, 'vehicle_number' : self.vehicle})
        
    def form_valid(self, formset):
        for form in formset:
            wheel = form.save(commit=False)
            wheel.vehicle_number = self.vehicle
            wheel.save()
        return HttpResponseRedirect(reverse('vehicle_list'))
    
class WheelUpdateView(LoginRequiredMixin, UpdateView):
    model = Wheel
    template_name = 'wheel_edit.html'
    form_class = WheelCreateForm
    
    def dispatch(self, request, *args, **kwargs):
        self.vehicle = Vehicle.objects.get(pk=self.kwargs['pk'])
        return super(WheelUpdateView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        qs = Wheel.objects.filter(vehicle_number=self.vehicle)
        wheels_form = forms.modelformset_factory(Wheel, WheelCreateForm, 
                                      fields=['serial_number','purchase_date','running_life'], extra=0,
                                      can_delete = False)(queryset=qs)
        return render(request, 'wheel_edit.html', {'wheels_form' : wheels_form, 'vehicle_number' : self.vehicle})
        
    def post(self, request, *args, **kwargs):
        formset = forms.modelformset_factory(Wheel, WheelCreateForm, 
                                      fields=['serial_number','purchase_date','running_life'], 
                                      can_delete = False)(request.POST or None)
        if formset.is_valid():
            return self.form_valid(formset)
        else:
            return render(request, 'wheel_edit.html', {'wheels_form' : formset, 'vehicle_number' : self.vehicle})
        
    def form_valid(self, formset):
        for form in formset:
            wheel = form.save(commit=False)
            wheel.vehicle_number = self.vehicle
            wheel.save()
        return HttpResponseRedirect(reverse('vehicle_list'))
    

### Maintenance Views ###

class MaintenanceListView(LoginRequiredMixin, ListView):
    model = VehicleMaintenance
    template_name = 'maintenance_list.html'    
    
class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    model = VehicleMaintenance
    form_class = MaintenanceCreateForm
    template_name = 'maintenance_create.html'    
    success_url = reverse_lazy('maintenance_list')
    success_message = "Maintenance Bill has been recorded successfully"

class MaintenanceUpdateView(LoginRequiredMixin, UpdateView):
    model = VehicleMaintenance
    form_class = MaintenanceCreateForm
    template_name = 'maintenance_edit.html'    
    success_url = reverse_lazy('maintenance_list')
    success_message = "Maintenance Bill has been edited successfully"
    
class MaintenanceDeleteView(LoginRequiredMixin, BSModalDeleteView):
    model = VehicleMaintenance
    template_name = 'maintenance_delete.html'
    error_template = 'maintenance_list.html'
    success_url = reverse_lazy('maintenance_list')
    success_message = ""

    def post(self, request, *args, **kwargs):
        try:
            post = self.delete(request, *args, **kwargs)
            messages.success(request,"Maintenance Invoice has been deleted successfully",extra_tags='success')
            return post
        except ProtectedError:
            messages.error(request,"You cannot delete this entry",extra_tags='danger')
            return redirect('maintenance_list')

@login_required    
def get_maintenance_listing(request):
    qs = list(VehicleMaintenance.objects.values_list('description',flat=True).distinct())
    return JsonResponse(qs, safe = False)    
    