from rest_framework import serializers
from create_user.models import User

class Registerserializers(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def save(self):
        account=User(
            username=self.validated_data['username'],
            email = self.validated_data['email'],
        )
        account.save()
        password=self.validated_data['password']
        password2 = self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({'password':'password must match'})
        account.set_password(password)
        account.save()
        return account
