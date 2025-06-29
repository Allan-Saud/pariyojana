from rest_framework import serializers
from projects.models.progress_stage import ProjectProgress

class ProjectProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgress
        fields = [
            'id', 'project', 'stage_key', 'stage_label',
            'is_completed', 'completed_at'
        ]
