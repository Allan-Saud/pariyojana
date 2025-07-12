from rest_framework import serializers
from projects.models.Installment_Payment.account_photos import AccountPhoto

class AccountPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountPhoto
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at',"recommendation" ,"project"]  # check_photo auto-filled from recommendation

    def create(self, validated_data):
        instance = AccountPhoto(**validated_data)
        instance.save()  # triggers save logic to fetch file from recommendation
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
