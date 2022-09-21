from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Client
from .serializers import ProjectSerializer
from accounts.permissions import IsAuthenticatedOwner


class ProjectViewSet(ModelViewSet):
    queryset = Client.objects.all().select_related('user')
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticatedOwner,)

    def list(self, request, *args, **kwargs):

        projects = Client.objects.filter(user=request.user)

        serializer = ProjectSerializer(projects, many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Rewrite a common create method to update request data with customer id.

        :param request: Request Object.
        :param args: arguments.
        :param kwargs: key work arguments.

        :return: Response object.
        """

        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        Rewrite a common destroy method to update request data with customer id.

        :param request: Request Object.
        :param args: arguments.
        :param kwargs: key work arguments.

        :return: Response object.
        """

        return super().destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Rewrite a common retrieve method to update request data with customer id.

        :param request: Request Object.
        :param args: arguments.
        :param kwargs: key work arguments.

        :return: Response object.
        """

        return super().retrieve(request, *args, **kwargs)