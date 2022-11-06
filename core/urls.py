from django.urls import path, include

urlpatterns = [
    path("", include("core.apiV1.urls.account")),
    path("", include("core.apiV1.urls.payment")),
    path("", include("core.apiV1.urls.income")),
]
