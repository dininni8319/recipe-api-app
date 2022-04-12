from django.contrib.auth import get_user_model, authenticate
#authenticate function is a django helper command for working with django authentication system
from django.utils.translation import ugettext_lazy as _ #this will automaticli convert all the languages into the correct language
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
    

class AuthTokenSerializer(serializers.Serializer): 
    """Serializer for the user authentication object"""
    email = serializers.CharField() 
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False #we want to make sure that the django framework doesn't trim of the white space
    )
    #validate function

    def validate(self, attrs):
        """Validate and autheticate the user"""
        email = attrs.get('email') #we are going to get the 
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'), #this is how you access to context of the request 
            username=email,
            password=password
        )

        # if the user is not authenticated will throw an error with 400 response
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs #whenever you overwiting the validate function you must return the values at the end