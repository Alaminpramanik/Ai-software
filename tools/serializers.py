from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from tools.models import EmailExtract, NumberExtract, DomainExtract, ImageToText,Content,Wrodcounter,ContentKeyword

from tools.task.finder import mail_process, number_process,domain_process,image_process,pdf_to_process ,article_process, grammer_process,word_count_process
from tools.task.generator import  article_process, content_write



class TextEmailFinderSerializer(ModelSerializer):
    email=serializers.CharField(max_length=100000, min_length=None)
    class Meta:
        model = EmailExtract
        fields = ['email']

    def create(self, validated_data):
        email=validated_data.get('email')
        email = mail_process(email)
    
        validated_data['email'] = email

        return validated_data



class TextNumberFinderSerializer(ModelSerializer):
    phone=serializers.CharField(max_length=100000, min_length=None)
    class Meta:
        model = NumberExtract
        fields = ['phone']

    def create(self, validated_data):
        phone=validated_data.get('phone')
        phone = number_process(phone)
    
        validated_data['phone'] = phone

        return validated_data



class DomainFinderSerializer(ModelSerializer):
    link=serializers.CharField(max_length=100000, min_length=None)
    class Meta:
        model = DomainExtract
        fields = ['link']

    def create(self, validated_data):
        link=validated_data.get('link')
        link = domain_process(link)
    
        validated_data['link'] = link

        return validated_data


class ImageToTextSerializer(ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    text=serializers.CharField(read_only=True)
    class Meta:
        model = ImageToText
        fields = ['image','text']

    def create(self, validated_data):
        image=validated_data.get('image')
        images = image_process(image)
        print('images',images)
    
        validated_data['image'] = image
        validated_data['text'] = images

        return validated_data



class PdftoJsonSerializer(ModelSerializer):
    file = serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    json=serializers.CharField(read_only=True)
    class Meta:
        model = Wrodcounter
        fields = ['file','json']

    def create(self, validated_data):
        pdf=validated_data.get('file')
        # print('pdf',pdf)
        json = pdf_to_process(pdf)
        # print('file',pdf)
    
        validated_data['file'] = pdf
        validated_data['text'] = json

        return validated_data



class WordCounterFinderSerializer(ModelSerializer):
    text=serializers.CharField(max_length=100000, min_length=None)
    class Meta:
        model = Wrodcounter
        fields = ['text']

    def create(self, validated_data):
        text=validated_data.get('text')
        text = word_count_process(text)
    
        validated_data['text'] = text

        return validated_data



class ArticleWriterSerializer(ModelSerializer):
    keyword=serializers.CharField(max_length=100, min_length=None)
    content=serializers.CharField(max_length=100000, min_length=None)

    class Meta:
        model = Content
        fields = ['keyword','content']

    def create(self, validated_data):
        keyword=validated_data.get('keyword')
        # print('keyword',keyword)
        content=validated_data.get('content')
        # print('content',content)
        content = article_process(keyword,content)
        print('content', content)
        validated_data['content'] = content
        # validated_data['content'] = content


        return validated_data


class ContentWriterSerializer(ModelSerializer):
    keyword=serializers.CharField(max_length=100, min_length=None)

    class Meta:
        model = ContentKeyword
        fields = ['keyword']

    def create(self, validated_data):
        keyword=validated_data.get('keyword')

        # print('keyword',keyword)
        keyword = content_write(keyword)
        # print('keyword', keyword)
        validated_data['keyword'] = keyword

        return validated_data



class GrammerWriterSerializer(ModelSerializer):
    article=serializers.CharField(max_length=100000, min_length=None)
    class Meta:
        model = Content
        fields = ['article']

    def create(self, validated_data):
        article=validated_data.get('article')
        article = grammer_process(article)
        print('article',article)
    
        validated_data['article'] = article

        return validated_data