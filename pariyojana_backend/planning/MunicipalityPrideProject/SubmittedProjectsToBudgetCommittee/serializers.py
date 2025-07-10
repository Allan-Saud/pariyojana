from rest_framework import serializers
from planning.MunicipalityPrideProject.SubmittedProjectsToBudgetCommittee.models import SubmittedToBudgetMunicipalityPrideProject

class SubmittedToBudgetMunicipalityPrideProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedToBudgetMunicipalityPrideProject
        fields = '__all__'
