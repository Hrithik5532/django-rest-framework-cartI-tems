from django.urls import path
from .views import cartview
urlpatterns = [
    path("cart-item",cartview.as_view()),
     path("cart-item/<int:id>",cartview.as_view())
]
