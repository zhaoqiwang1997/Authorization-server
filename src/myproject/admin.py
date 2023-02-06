from django.contrib import admin
from .models import Card, User, Company

# show model in the admin interface
admin.site.register(Card)
admin.site.register(User)
admin.site.register(Company)
