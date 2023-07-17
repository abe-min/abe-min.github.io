from rest_framework import serializers

from .models import Profile

class profileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('General', 'Business', 'Entertainment', 'Health', 'Science', 'Sports', 'Technology')


