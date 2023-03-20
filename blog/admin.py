from django.contrib import admin
from .models import BlogInfo, About, Privacy, Terms, Support
# Register your models here.


admin.site.register(BlogInfo)
admin.site.register(About)
admin.site.register(Privacy)
admin.site.register(Terms)
admin.site.register(Support)