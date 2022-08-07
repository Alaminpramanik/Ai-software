from django.shortcuts import render,  get_object_or_404, redirect
from requests import request
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from tools.serializers import TextEmailFinderSerializer,TextNumberFinderSerializer, DomainFinderSerializer,ImageToTextSerializer,ArticleWriterSerializer,GrammerWriterSerializer,WordCounterFinderSerializer,PdftoJsonSerializer



def PramanikSoft(request):
    templates='../templates/textdomfind.html'
    return render(request, templates)

def RewriteAPIView(request):
 
    templates = '../templates/rewrite.html'
    return render(request, templates)


class TextMailFinderAPIView(CreateAPIView):
    serializer_class = TextEmailFinderSerializer
    permission_classes = (AllowAny,)

class WordCounterAPIView(CreateAPIView):
    serializer_class = WordCounterFinderSerializer
    permission_classes = (AllowAny,)

class NumberFinderAPIView(CreateAPIView):
    serializer_class = TextNumberFinderSerializer
    permission_classes = (AllowAny,)


class DomainFinderAPIView(CreateAPIView):
    serializer_class = DomainFinderSerializer
    permission_classes = (AllowAny,)

class ImageToTextAPIView(CreateAPIView):
    serializer_class = ImageToTextSerializer
    permission_classes = (AllowAny,)

class PDFToJsonAPIView(CreateAPIView):
    serializer_class = PdftoJsonSerializer
    permission_classes = (AllowAny,)

class AryticleWriterAPIView(CreateAPIView):
    serializer_class = ArticleWriterSerializer
    permission_classes = (AllowAny,)


class GrammerWriterAPIView(CreateAPIView):
    serializer_class = GrammerWriterSerializer
    permission_classes = (AllowAny,)