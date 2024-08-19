from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ServicesViewSet, UserViewSet, StaffsViewSet, BlogViewSet, AboutViewSet, ApplicationsViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="api Stocker",
        default_version='v1',
        description="ExaM Project Stocker",
        terms_of_service="Terms",
        contact=openapi.Contact(email="nchoriyev43@gmail.com"),
        license=openapi.License(name="License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'services-web', ServicesViewSet, basename='services-web')
router.register(r'users-web', UserViewSet, basename='users-web')
router.register(r'staffs-web', StaffsViewSet, basename='staffs-web')
router.register(r'blogs-web', BlogViewSet, basename='blogs-web')
router.register(r'abouts-web', AboutViewSet, basename='abouts-web')
router.register(r'applications-web', ApplicationsViewSet, basename='applications-web')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
