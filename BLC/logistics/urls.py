from django.urls import path
from logistics import views

urlpatterns = [
    ### Login & Logout Url ###
    path('', views.Login_Page.as_view(), name='login_page'),
    path('logout', views.Logout_Page.as_view(), name='logout_page'),
    ### Dashboard Url ###
    path('dashboard', views.Dashboard_Page.as_view(), name='dashboard'),
    ### Customer Url ###
    path('customer-list', views.CustomerListView.as_view(), name='customer_list'),
    path('customer-create', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customer-edit/<int:pk>', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer-delete/<int:pk>', views.CustomerDeleteView.as_view(), name='customer_delete'),
    ### Destination Url ###
    path('destination-list', views.DestinationListView.as_view(), name='destination_list'),
    path('destination-create', views.DestinationCreateView.as_view(), name='destination_create'),
    path('destination-edit/<int:pk>', views.DestinationUpdateView.as_view(), name='destination_edit'),
    path('destination-delete/<int:pk>', views.DestinationDeleteView.as_view(), name='destination_delete'),
    ### Vehicle Url ###
    path('vehicle-list', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle-create', views.VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicle-edit/<int:pk>', views.VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('vehicle-delete/<int:pk>', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
    ### Driver Url ###
    path('driver-list', views.DriverListView.as_view(), name='driver_list'),
    path('driver-create', views.DriverCreateView.as_view(), name='driver_create'),
    path('driver-edit/<int:pk>', views.DriverUpdateView.as_view(), name='driver_edit'),
    path('driver-delete/<int:pk>', views.DriverDeleteView.as_view(), name='driver_delete'),
    ### Routes Url ###
    path('route-list', views.RouteListView.as_view(), name='route_list'),
    path('route-create', views.RouteCreateView.as_view(), name='route_create'),
    path('route-edit/<int:pk>', views.RouteUpdateView.as_view(), name='route_edit'),
    path('route-delete/<int:pk>', views.RouteDeleteView.as_view(), name='route_delete'),
    ### Trip Url ###
    path('ongoing-trip-list', views.OngoingTripListView.as_view(), name='ongoing_trip_list'),
    path('completed-trip-list', views.CompletedTripListView.as_view(), name='completed_trip_list'),
    path('trip-create', views.TripCreateView.as_view(), name='trip_create'),
    path('trip-edit/<int:pk>', views.TripUpdateView.as_view(), name='trip_edit'),
    path('trip-delete/<int:pk>', views.TripDeleteView.as_view(), name='trip_delete'),
    path('trip-details/<int:pk>', views.TripDetailView.as_view(), name='trip_details'),
    path('trip-pending', views.TripPendingListView, name='trip_pending'),
    path('trip-close', views.TripCloseView.as_view(), name='trip_close'),
    path('product-autocomplete', views.get_product_listing, name='product_autocomplete'),
    path('get-available-vehicles', views.get_available_vehicles, name='get_available_vehicles'),
]