# from django.urls import path
# from .views import startup_detail

# urlpatterns = [
#     path('<slug:slug>/', startup_detail, name='startup_detail'),
# ]

from django.urls import path
from .views import startup_detail, submit_startup, submission_thanks, startup_list_grouped


urlpatterns = [
    path('submit/', submit_startup, name='submit_startup'),         # ✅ specific goes first
    path('thanks/', submission_thanks, name='submission_thanks'),   # ✅ add this too
    path('', startup_list_grouped, name='startup_list'),
    path('magazine/', startup_list_grouped, name='startup_magazine'),
    path('<slug:slug>/', startup_detail, name='startup_detail'),    # ✅ wildcard goes last
]

