from rest_framework import serializers
from account.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta():
        model = User
        fields = ['email', 'username', 'password', 'confirm_password', 'Is_User']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(
            email = self.validated_data['email'].lower(),
            username = self.validated_data['username'],
            Is_User=self.validated_data['Is_User'],
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Password must match.'})
        account.set_password(password)
        account.save()
        return account

        
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=20)
    class Meta:
        fields=['username','password']