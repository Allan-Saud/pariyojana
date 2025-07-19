# # projects/serializers/official_detail.py

from rest_framework import serializers
from projects.models.Consumer_Committee.official_detail import OfficialDetail
class OfficialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialDetail
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'project']
        extra_kwargs = {
            'serial_no': {'required': False, 'allow_null': True},
            'post': {'required': False, 'allow_null': True},
            'full_name': {'required': False, 'allow_null': True},
            'address': {'required': False, 'allow_null': True},
            'contact_no': {'required': False, 'allow_null': True},
            'gender': {'required': False, 'allow_null': True},
            'citizenship_no': {'required': False, 'allow_null': True},
            'citizenship_front': {'required': False, 'allow_null': True},
            'citizenship_back': {'required': False, 'allow_null': True},
        }

    def validate(self, data):
        project = data.get('project') or (self.instance.project if self.instance else None)
        post = data.get('post') or (self.instance.post if self.instance else None)

        unique_posts = ['अध्यक्ष', 'सचिव', 'कोषाध्यक्ष']
        if project and post in unique_posts:
            existing = OfficialDetail.objects.filter(project=project, post=post)
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise serializers.ValidationError(f"{post} already exists for this project.")
        return data
