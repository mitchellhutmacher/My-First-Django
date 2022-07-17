from django.contrib import admin
from .models import Question

# Register your models here.
# Register the question on the admin site
admin.site.register(Question)
