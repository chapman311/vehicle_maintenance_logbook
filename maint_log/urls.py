from django.urls import path, include

from . import views

app_name = 'maint_log'

urlpatterns = [
    path('', views.index, name='index'),
    
    path('get-vehicles/', views.getVehicles),
    path('add-vehicle/', views.addVehicle),
    path('get-maintenance-logs/<int:id>/', views.getMaintenanceLogs),
    path('add-maintenance-log/', views.addMaintenanceLog), 
    path('delete-maintenance-log/<int:id>', views.deleteMaintenanceLog), 
    path('user-login/', views.userLogin, name='user-login'),
    path('user-signup/', views.userSignUp, name='user-signup'),
    path('user-logout/', views.userLogout)
]