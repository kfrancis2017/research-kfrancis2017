from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Import your views

# URL patterns
urlpatterns = [    
    # Admin site URL
    path('admin/', admin.site.urls),
    
    # Add a view for the root catalog URL
    path('', views.index, name='catalog_index'),  # This will handle requests to 'catalog/'
    
    # Counter-related views
    path('counter/', views.index, name='counter'),  # Keeping this for additional functionality
    path('increment/', views.increment_counter, name='increment_counter'),
    
    # Save entry view
    path('save_counter/', views.save_counter, name='save_counter'),
]

# Serve static files during development
if settings.DEBUG:  # Ensure it only runs in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
