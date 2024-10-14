"""
URL configuration for locallibrary project.
"""

from django.urls import include, path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from catalog import views  # Import your views

# Catalog application
urlpatterns = [
    # Redirect base URL to catalog application
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
    
    # Include the catalog app's URLs
    path('catalog/', include('catalog.urls')),
]

# Counter functionality
# Assign distinct paths to avoid conflict with catalog URLs
urlpatterns += [
    path('counter/', views.index, name='counter'),
    path('increments/', views.increment_counter, name='increment_counter'),
    path('save_counter/', views.save_counter, name='save_counter'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
