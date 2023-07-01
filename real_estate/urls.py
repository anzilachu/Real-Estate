from django.contrib import admin
from django.urls import path
from listings.views import listings_list , listings_retrieve , listings_create , listings_update , listings_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listings_list),
    path('listings/<pk>/', listings_retrieve),
    path('create/', listings_create),
    path('listings/<pk>/update/', listings_update),
    path('listings/<pk>/delete/', listings_delete),
]
