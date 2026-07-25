from django.urls import path
from .views import RecommendBoxAPIView , ProductListAPIView , BoxListAPIView

urlpatterns = [

    path(
        "recommend-box/",
        RecommendBoxAPIView.as_view()
    ),
    path("products/", ProductListAPIView.as_view(), name="products"),
    path("boxes/", BoxListAPIView.as_view(), name="boxes"),

]