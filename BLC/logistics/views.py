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
from django.db.models import Q, Max
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
                    trip.complete = True
                    trip.end_date = dates[id_index]
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