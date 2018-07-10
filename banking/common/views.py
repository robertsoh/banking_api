from rest_framework.response import Response
from rest_framework.views import APIView


class ViewWrapper(APIView):

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
