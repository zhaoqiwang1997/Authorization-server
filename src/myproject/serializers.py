from rest_framework import serializers
from .models import Card, User, Company

# convert objects to JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_name', 'com_name', 'user_permission', 'user_cards']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['card_number', 'user_name', 'com_name', 'expiration_data', 'masked_number', 'limit', 'balance']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['com_name', 'users', 'cards']