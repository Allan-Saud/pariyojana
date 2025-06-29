from rest_framework import serializers
from projects.models.ExtendedDeadline.extended_deadline import ExtendedDeadline

class ExtendedDeadlineSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField(write_only=True)
    project_name = serializers.CharField(source='agreement.project.name', read_only=True)
    previous_completion_date = serializers.DateField(read_only=True)

    class Meta:
        model = ExtendedDeadline
        fields = [
            'id',
            'project_id',
            'project_name',
            'previous_completion_date',
            'extended_completion_date',
            'reason',
            'created_at'
        ]

    def create(self, validated_data):
        project_id = validated_data.pop('project_id')
        from projects.models.Project_Aggrement.project_aggrement_details import ProjectAgreementDetails

        try:
            agreement = ProjectAgreementDetails.objects.get(project=project_id)  # <-- here
        except ProjectAgreementDetails.DoesNotExist:
            raise serializers.ValidationError("Agreement not found for this project.")

        return ExtendedDeadline.objects.create(agreement=agreement, **validated_data)

