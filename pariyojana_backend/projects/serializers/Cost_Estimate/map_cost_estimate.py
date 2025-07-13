from rest_framework import serializers
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from authentication.models import VerificationLog
# class MapCostEstimateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MapCostEstimate
#         fields = '__all__'
#         read_only_fields = ['created_at', 'updated_at', 'status', 'is_verified','project']
        
#     def create(self, validated_data):
#         file = validated_data.get("file")
#         if file:
#             validated_data["status"] = "अपलोड गरिएको"
#         return super().create(validated_data)

#     def update(self, instance, validated_data):
#         file = validated_data.get('file', instance.file)
#         checker = validated_data.get('checker')
#         approver = validated_data.get('approver')
    
#          # Step 1: If no file is uploaded but checker/approver is set, raise error
#         if not file and (checker or approver):
#             raise ValidationError("फाइल अपलोड नगरि चेक/अप्रुभर राख्न मिल्दैन।")

#         # Step 2: If file uploaded for the first time, set status
#         if file and not instance.file:
#             instance.status = "अपलोड गरिएको"

#         # Step 3: If file already exists, and both checker and approver are being set
#         if file and checker and approver:
#             instance.status = "चेक जाँचको लागी पठाइएको"
#             instance.is_verified = True

#         return super().update(instance, validated_data)


class MapCostEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapCostEstimate
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'status', 'is_verified', 'project']

    def create(self, validated_data):
        file = validated_data.get("file")
        checker = validated_data.get("checker")
        approver = validated_data.get("approver")

        # Don't create VerificationLog here
        if not file and (checker or approver):
            raise ValidationError("फाइल अपलोड नगरि चेक/अप्रुभर राख्न मिल्दैन।")

        if file:
            validated_data["status"] = "अपलोड गरिएको"

        return super().create(validated_data)  # No VerificationLog here

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user if request else None

        new_file = validated_data.get("file", None)
        new_checker = validated_data.get("checker", None)
        new_approver = validated_data.get("approver", None)

        file_exists = new_file or instance.file

        if not file_exists and (new_checker or new_approver):
            raise ValidationError("फाइल अपलोड नगरि चेक/अप्रुभर राख्न मिल्दैन।")

        if new_file and not instance.file:
            validated_data["status"] = "अपलोड गरिएको"

        # Only create log if checker AND approver are BOTH newly set
        creating_log = (
            file_exists and
            "checker" in validated_data and
            "approver" in validated_data and
            validated_data["checker"] is not None and
            validated_data["approver"] is not None and
            not instance.is_verified
        )

        if creating_log:
            validated_data["status"] = "चेक जाँचको लागी पठाइएको"
            validated_data["is_verified"] = True

        instance = super().update(instance, validated_data)

        if creating_log:
            VerificationLog.objects.create(
                project=instance.project,
                file_title=instance.title,
                file_path=instance.file.url if instance.file else '',
                # uploader_role="अपलोड कर्ता",
                # uploader = user.full_name if user else '',
                uploader_name = user.full_name,
                uploader_role = user.role,
                status=instance.status,
                remarks=instance.remarks,
                checker=instance.checker,
                approver=instance.approver,
                source_model='MapCostEstimate',
                source_id=instance.id
            )

        return instance



