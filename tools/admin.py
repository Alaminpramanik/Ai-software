from django.contrib import admin

from tools.models import EmailExtract,ImageToText, DomainExtract, NumberExtract,Content,ContentKeyword


admin.site.register(EmailExtract)
admin.site.register(ContentKeyword)
admin.site.register(Content)
admin.site.register(ImageToText)
admin.site.register(DomainExtract)
admin.site.register(NumberExtract)