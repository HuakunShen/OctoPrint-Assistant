from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('printer/state/', views.octoprint_state, name='printer state'),
    path('job/status/', views.octoprint_job_status, name='job status'),
    path('job/cancel/', views.octoprint_job_cancel, name='cancel job'),
    path('job/toggle/', views.octoprint_job_toggle, name='toggle job'),
    path('job/start/', views.octoprint_job_start, name='start job'),
    path('connect/', views.octoprint_connect, name='connect octoprint to 3D printer'),
    path('disconnect/', views.octoprint_disconnect, name='disconnect octoprint to 3D printer'),
]