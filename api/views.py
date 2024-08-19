from rest_framework.response import Response
from rest_framework.decorators import action
from .helpers import StatusChoicesStaff, StatusChoicesPb
from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import TokenAuthentication


from .models import User, Staffs, ServicesCategory, Services, Blog, About, Applications
from .serializers import UserSerializer, StaffsSerializer, ServicesCategorySerializer, ServicesSerializer, \
    BlogSerializer, AboutSerializer, ApplicationsSerializer

class ServicesCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ServicesCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_b = [filters.SearchFilter]
    search_fields = ['name', 'slug']

    def get_queryset(self):
        return ServicesCategory.objects.filter(status='PUBLIC')
class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_b = [filters.SearchFilter]
    search_fields = ['name', 'id', 'slug']

    def get_queryset(self):
        return Services.objects.filter(status='PUBLIC')

    @action(detail=True, methods=['POST'])
    def count_services(self, request, slug=None):
        service = self.get_object()
        service.views += 1
        service.save()
        return Response(data={'Counted': service.views})

    @action(detail=True, methods=['GET'])
    def to_draft(self, request, *args, **kwargs):
        service = self.get_queryset()
        for servic in service:
            servic.pb_to_df()
        return Response(data={'message': 'all services were changed to draft'})

    @action(detail=True, methods=['GET'])
    def to_publish(self, request, *args, **kwargs):
        service = Services.objects.all()
        for servic in service:
            servic.df_to_pb()
        return Response(data={'message': 'all services status were changed to public'})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email', 'phone_number']

    @action(detail=False, methods=['GET'])
    def active_users(self, request, *args, **kwargs):
        active_users = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(active_users, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def staff_members(self, request, *args, **kwargs):
        staff_members = self.get_queryset().filter(groups__name='Staff')
        serializer = self.get_serializer(staff_members, many=True)
        return Response(serializer.data)


class StaffsViewSet(viewsets.ModelViewSet):
    queryset = Staffs.objects.all()
    serializer_class = StaffsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'name']

    def get_queryset(self):
        return Blog.objects.filter(status='PUBLIC')

    @action(detail=True, methods=['POST'])
    def count_services(self, request, slug=None):
        blog = self.get_object()
        blog.views += 1
        blog.save()
        return Response(data={'Counted': blog.views})

    @action(detail=True, methods=['GET'])
    def to_draft(self, request, *args, **kwargs):
        blogs = self.get_queryset()
        for blog in blogs:
            blog.pb_to_df()
        return Response(data={'message': 'all blogs were changed to draft'})

    @action(detail=True, methods=['GET'])
    def to_publish(self, request, *args, **kwargs):
        blogs = self.get_queryset()
        for blog in blogs:
            blog.df_to_pb()
        return Response(data={'message': 'all blogs were changed to PUBLIC'})

    @action(detail=True, methods=['GET'])
    def admin_users(self, request, *args, **kwargs):
        blogs = self.get_queryset().filter(admin__username='admin')
        serializer = self.get_serializer(blogs, many=True)
        return Response(serializer.data)


class AboutViewSet(viewsets.ModelViewSet):
    serializer_class = AboutSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug']

    def get_queryset(self):
        return About.objects.filter(status='PUBLIC')

    @action(detail=True, methods=['GET'])
    def to_draft(self, request, *args, **kwargs):
        abouts = self.get_queryset()
        for about in abouts:
            about.pb_to_df()
        return Response(data={'message': 'Description removed to draft mode'})

    @action(detail=True, methods=['GET'])
    def to_draft(self, request, *args, **kwargs):
        abouts = self.get_queryset()
        for about in abouts:
            about.df_to_pb()
        return Response(data={'message': 'Description removed to public mode'})


class ApplicationsViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationsSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['slug', 'full_name']

    def get_queryset(self):
        return Applications.objects.filter(status='PUBLIC')

    @action(detail=True, methods=['GET'])
    def to_draft(self, request, *args, **kwargs):
        applications = self.get_queryset()
        for application in applications:
            application.pb_to_df()
        return Response(data={'message': 'Application removed to draft'})

    @action(detail=True, methods=['GET'])
    def to_publish(self, request, *args, **kwargs):
        applications = self.get_queryset()
        for application in applications:
            application.df_to_pb()
        return Response(data={'message': 'Description removed to public'})