from mainapp import views
from django.urls import path
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('courses/', views.CourserListView.as_view(), name='courses'),
    path('doc_site/', views.DocSiteView.as_view(), name='docsite'),
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsView.as_view(), name='news'),

    # Logs
    path('logs/', views.LogView.as_view(), name='logs'),
    path('logs/download', views.LogDownloadView.as_view(), name='logs_download'),
]
