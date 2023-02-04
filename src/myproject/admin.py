from django.contrib import admin
from .models import Card, User, Company

admin.site.register(Card) # show model in the admin interface
admin.site.register(User)
admin.site.register(Company)
