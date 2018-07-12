from rest_framework import parsers, renderers
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from banking.customers.models import ORMCustomer


class ViewWrapper(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    view_creator_func = None

    def post(self, request, *args, **kwargs):
        body, status = self.view_creator_func(request, **kwargs).post(request.data)
        return Response(body, status=status, content_type='application/json')

    def get(self, request, *args, **kwargs):
        kwargs.update(request.GET.dict())
        body, status = self.view_creator_func(request, **kwargs).get(**kwargs)
        return Response(body, status=status, content_type='application/json')

    def patch(self, request, *args, **kwargs):
        kwargs.update(request.data)
        body, status = self.view_creator_func(request, **kwargs).patch(kwargs)
        return Response(body, status=status, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        body, status = self.view_creator_func(request, **kwargs).delete(**kwargs)
        return Response(body, status=status, content_type='application/json')


class CustomObtainAuthTokenAPIView(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        customer = ORMCustomer.objects.get(user=user)
        return Response({
            'access_token': token.key,
            'customer_id': customer.id,
            'customer_full_name': customer.full_name()
        })