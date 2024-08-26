from django.shortcuts import render
from django.http import HttpResponse
from  .models import pdata
from rest_framework.decorators import api_view
from .serializers import sec
from  rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView,GenericAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
def display(self):
    return HttpResponse("Hello Student")

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def std(self):
    qs=pdata.objects.all()
    sc=sec(qs,many=True)
    return Response({'data':sc.data})

class apiv(APIView):
    def get(self,request,tt=None):
        qs=pdata.objects.filter(id=tt)
        sc=sec(qs,many=True)
        return Response({"data":sc.data})
    def post(self,request):
        qs = pdata.objects.all()
        sc = sec(qs, many=True)
        return Response({"data": sc.data})
    def put(self,request):
        qs = pdata.objects.all()
        sc = sec(qs, many=True)
        return Response({"data": sc.data})
    def patch(self,request):
        qs = pdata.objects.all()
        sc = sec(qs, many=True)
        return Response({"data": sc.data})
    def delete(self,request):
        qs = pdata.objects.all()
        sc = sec(qs, many=True)
        return Response({"data": sc.data})

class list(ListAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
class create(CreateAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec

class retrieve(RetrieveAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
class update(UpdateAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
class destroy(DestroyAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
    
class lc(ListCreateAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
class ru(RetrieveUpdateAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
class rd(RetrieveDestroyAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec
class rud(RetrieveUpdateDestroyAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec


from rest_framework import mixins


class lmm(mixins.ListModelMixin,GenericAPIView):
    queryset=pdata.objects.all()
    serializer_class=sec

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)