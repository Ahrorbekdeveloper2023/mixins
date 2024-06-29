from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .models import Klass, Mehmonxona, Travel
from .seriallizer import KlassSerializer, MehmonxonaSerializer, TravelSerializer



class KlassCreateAPIView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):

    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class KlassUpdateDeleteAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericAPIView):

    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class MehmonxonaCreateAPIView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):

    queryset = Mehmonxona.objects.all()
    serializer_class = MehmonxonaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MehmonxonaUpdateDeleteAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericAPIView):

    queryset = Mehmonxona.objects.all()
    serializer_class = MehmonxonaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class TravelCreateAPIView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TravelUpdateDeleteAPIView(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

