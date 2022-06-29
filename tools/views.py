from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from tools.serializers import TextEmailFinderSerializer,TextNumberFinderSerializer, DomainFinderSerializer,ImageToTextSerializer,ArticleWriterSerializer,GrammerWriterSerializer
from tools.models import EmailExtract, NumberExtract, DomainExtract, ImageToText,AutomaticArticle


#website to mail find(website mail scrap)
class TextMailFinderAPIView(CreateAPIView):
    serializer_class = TextEmailFinderSerializer
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

class AryticleWriterAPIView(CreateAPIView):
    serializer_class = ArticleWriterSerializer
    permission_classes = (AllowAny,)


class GrammerWriterAPIView(CreateAPIView):
    serializer_class = GrammerWriterSerializer
    permission_classes = (AllowAny,)