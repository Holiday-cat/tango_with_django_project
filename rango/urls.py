from django.urls import path
from rango import views
from django.conf import settings 
from django.conf.urls.static import static


app_name = 'rango'


urlpatterns = [ 
    path('', views.index, name='index'),
    path('about/', views.about, name="about"),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'), 
	path('add_category/', views.add_category, name='add_category'),
]

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #views.show_category, name='show_category'),