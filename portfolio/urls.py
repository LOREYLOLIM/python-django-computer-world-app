from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'index'),
    path('portfolio/', views.portfolio, name = 'portfolio'),
    path('details/<int:pk>', views.details, name = 'details'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('courses/', views.courses, name = 'courses'),
    path('testimonial/', views.testimonial, name = 'testimonial'),
    path('testimonial/delete/<int:id>', views.delete, name = 'delete_testimonial'),
    path('services/', views.services, name = 'services'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('FAQS/', views.FAQs, name = 'FAQs'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)