from django.contrib.auth import get_user_model

from rest_framework import serializers 

#Django framework has a bildin serializer that we can use
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""
     #With ModelSerializer we need to specify the class meta, the first linwe you need to specify the model that you wanna base the ModelSerializer from
    class Meta: 
        model = get_user_model() #returns the user model class
        # the fields that we want to make accesseble
        fields = ('email', 'password', 'name')
        #extra keywords args, allows us to config few extra settings in our ModelSerializer, to insure that the password is write only and that the menimum required length is 5 characters 
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)
        