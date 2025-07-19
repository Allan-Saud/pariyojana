# # projects/serializers/official_detail.py

from rest_framework import serializers
from projects.models.Consumer_Committee.official_detail import OfficialDetail

class OfficialDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialDetail
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at','project']

    def validate(self, data):
        project = data.get('project') or self.instance.project
        post = data.get('post') or self.instance.post

        # Enforce only one अध्यक्ष, सचिव, कोषाध्यक्ष per project
        unique_posts = ['अध्यक्ष', 'सचिव', 'कोषाध्यक्ष']
        if post in unique_posts:
            existing = OfficialDetail.objects.filter(
                project=project, post=post
            )
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise serializers.ValidationError(f"{post} already exists for this project.")

        return data
