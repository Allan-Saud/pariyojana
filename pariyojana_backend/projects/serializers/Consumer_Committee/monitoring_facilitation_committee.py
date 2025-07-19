from rest_framework import serializers
from projects.models.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeMember

class MonitoringFacilitationCommitteeMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitoringFacilitationCommitteeMember
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, data):
        post = data.get('post') or self.instance.post
        project = data.get('project') or self.instance.project

        unique_posts = ['संयोजक', 'सदस्य सचिव']
        if post in unique_posts:
            existing = MonitoringFacilitationCommitteeMember.objects.filter(project=project, post=post)
            if self.instance:
                existing = existing.exclude(pk=self.instance.pk)
            if existing.exists():
                raise serializers.ValidationError(f"{post} already exists for this project.")
        
        return data