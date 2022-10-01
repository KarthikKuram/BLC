from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from decimal import *
from datetime import datetime,timedelta,date
# Create your models here.
class CaseInsensitiveFieldMixin:
    """
    Field mixin that uses case-insensitive lookup alternatives if they exist.
    """

    LOOKUP_CONVERSIONS = {
        'exact': 'iexact',
        'contains': 'icontains',
        'startswith': 'istartswith',
        'endswith': 'iendswith',
        'regex': 'iregex',
    }

    def get_lookup(self, lookup_name):
        converted = self.LOOKUP_CONVERSIONS.get(lookup_name, lookup_name)
        return super().get_lookup(converted)

class CICharField(CaseInsensitiveFieldMixin, models.CharField):
    pass

# Regular Expression for Vehicle Number #
vehicle_number = RegexValidator(r'^[A-Za-z]{2}-[0-9]{2}-[A-Za-z]{2}-[0-9]{4}')
mobile_number = RegexValidator(r'^[0-9]{10}')


### CUSTOMER MODEL ###
class Customer(models.Model):
    name = CICharField(max_length=255, unique=True)
    address = models.TextField(max_length=255)
    state = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
    
    def __str__(self):
        return self.name    
    
### DESTINATION MODEL ###
class Destination(models.Model):
    name = CICharField(max_length=255, unique=True)
    address = models.TextField(max_length=255)
    state = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"
    
    def __str__(self):
        return self.name    

### DRIVER MODEL ###    
class Driver(models.Model):
    full_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=10, unique=True, validators=[mobile_number])
    available = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
    
    def __str__(self):
        return self.full_name
    
    
### AXLE CHOICES ###
class Axle(models.IntegerChoices):
    WL12 = 12, '12WL'
    WL14 = 14, '14WL'
    WL16 = 16, '16WL'
    WL22 = 22, '22WL'
       
### VEHICLE MODEL ###
class Vehicle(models.Model):
    vehicle_number = CICharField(max_length=13, unique=True, validators=[vehicle_number])
    purchase_date = models.DateField()
    axle = models.IntegerField(choices=Axle.choices)
    fuel_capacity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    load_capacity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        
    def __str__(self):
        return self.vehicle_number
    
### TRIP DISTANCE MODEL ###
class Route(models.Model):
    customer = models.ForeignKey('logistics.Customer', on_delete=models.CASCADE, related_name='route_customers')    
    destination = models.ForeignKey('logistics.Destination', on_delete=models.CASCADE, related_name='route_destinations')
    distance = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    fuel_required = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    
    class Meta:
        verbose_name = "Route"
        verbose_name_plural = "Routes"
    
    def __str__(self):
        return '%s --->To---> %s' % (self.customer, self.destination)

### WHEEL USAGE MODEL ###
class Wheel(models.Model):
    vehicle_number = models.ForeignKey('logistics.Vehicle', on_delete=models.PROTECT, related_name='vehicle_wheels')
    serial_number = models.CharField(max_length=255, unique=True, blank=True, null=True)
    purchase_date = models.DateField(blank=True, null=True)
    running_life = models.IntegerField(validators=[MinValueValidator(1)],blank=True, null=True)
    usage = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))], default=0)
    
    class Meta:
        verbose_name = "Wheel"
        verbose_name_plural = "Wheels"
        
    def __str__(self):
        return '%s || %s' % (self.vehicle_number, self.serial_number)    
    
    # @property
    # def usage(self):
    #     total_run=0
    #     total_trips = self.vehicle_number.vehicle_trips.all()
    #     for trip in total_trips:
    #         total_run+=trip.route.distance
    #     return total_run
            
    
### VEHICLE MAINTENANCE MODEL ###
class VehicleMaintenance(models.Model):
    vehicle_number = models.ForeignKey('logistics.Vehicle', on_delete=models.PROTECT, related_name='vehicle_maintenance')
    start_date = models.DateField()    
    end_date = models.DateField()
    description = models.TextField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    
    class Meta:
        verbose_name = "VehicleMaintenance"
        verbose_name_plural = "VehicleMaintenances"
        
### TRIP MODEL ###
def increment_trip_number():
  last_no = Trip.objects.all().order_by('id').last()
  if not last_no:
    return 'BLC-' + str(date.today().month).zfill(2) +'-'+ str(date.today().year) + '-' + '0001'
  no_int = int(last_no.trip_id[-4:])
  new_no_int = no_int + 1
  new_no_id = 'BLC-' + str(date.today().month).zfill(2) +'-'+ str(date.today().year) +'-'+ str(new_no_int).zfill(4)  
  return new_no_id

class Trip(models.Model):
    trip_id = CICharField(max_length=50, blank=True, unique=True, default=increment_trip_number)
    route = models.ForeignKey('logistics.Route', on_delete=models.PROTECT, related_name='trip_route')
    vehicle_number = models.ForeignKey('logistics.Vehicle',on_delete=models.PROTECT, related_name='vehicle_trips')    
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    driver = models.ForeignKey('logistics.Driver', on_delete=models.PROTECT, related_name='driver_trips')
    product = models.CharField(max_length=255)
    load = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    message_id = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    complete = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"
        
    def __str__(self):
        return '%s || %s' % (self.trip_id, self.route)    
    
### FUEL MODEL ###
class Fuel(models.Model):
    vehicle_number = models.ForeignKey('logistics.Vehicle', on_delete=models.PROTECT, related_name='vehicle_fuel')
    driver = models.ForeignKey('logistics.Driver', on_delete=models.PROTECT, related_name='driver_fuel')
    date = models.DateField()
    station = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])    
    rate = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    bill = models.ImageField(blank=True, upload_to='fuel_bills')
    
    class Meta:
        verbose_name = "Fuel"
        verbose_name_plural = "Fuels"
        
    def __str__(self):
        return self.date + " || " + self.station + " || " + str(self.quantity)