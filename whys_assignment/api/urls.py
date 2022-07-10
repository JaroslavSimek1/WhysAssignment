from django.urls import path
from . import views


urlpatterns = [
    path('',views.apiOverview, name = 'apiOverview'),
    path('detail/<slug:name>/',views.records, name = 'records'),
    path('detail/<slug:name>/<int:id>',views.detailOfRecord, name = 'detailOfRecord'),
    path('import',views.importData, name = 'importData')
    
]