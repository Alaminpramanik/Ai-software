from django.contrib import admin

from tools.models import EmailExtract,AutomaticArticle,ImageToText, DomainExtract, NumberExtract,ArticleCategory


admin.site.register(EmailExtract)
admin.site.register(AutomaticArticle)
admin.site.register(ArticleCategory)
admin.site.register(ImageToText)
admin.site.register(DomainExtract)
admin.site.register(NumberExtract)