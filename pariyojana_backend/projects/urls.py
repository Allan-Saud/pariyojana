from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views.project import ProjectViewSet
from projects.views.initiation_process import InitiationProcessViewSet
from projects.views.program_detail import ProgramDetailViewSet
from projects.views.beneficiary_details import BeneficiaryDetailViewSet
from projects.views.consumer_committee_details import ConsumerCommitteeDetailViewSet
from projects.views.monitoring_facilitation_committee import MonitoringFacilitationCommitteeViewSet
from projects.views.cost_estimate_detail import CostEstimateDetailViewSet
from projects.views.consumer_committee import (
    ConsumerCommitteeListView,
    consumer_committee_upload,
    download_consumer_committee_pdf,
)
from projects.views.consumer_committee import preview_template
from projects.views.project_aggrement_details import ProjectAgreementDetailsViewSet
from projects.views.official_detail import OfficialDetailViewSet
from projects.views.operation_location import OperationSitePhotoViewSet


router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'initiation-process', InitiationProcessViewSet)
router.register(r'program-details', ProgramDetailViewSet, basename='program-detail')
router.register(r'beneficiaries', BeneficiaryDetailViewSet, basename='beneficiaries')
router.register(r'consumer-committee-details', ConsumerCommitteeDetailViewSet)
router.register(r'official-details', OfficialDetailViewSet, basename='official-detail')
router.register(r'monitoring-committee', MonitoringFacilitationCommitteeViewSet, basename='monitoring-committee')
router.register(r'cost-estimate-details', CostEstimateDetailViewSet, basename='cost-estimate-details')
router.register(r'project-agreement-details', ProjectAgreementDetailsViewSet, basename='project-agreement-details')
router.register(r'operation-site-photos', OperationSitePhotoViewSet, basename='operation-site-photos')

urlpatterns = [
    path('', include(router.urls)),

    # Consumer Committee
    path('consumer-committee/', ConsumerCommitteeListView.as_view(), name='consumer-committee-list'),
    path('consumer-committee/upload/', consumer_committee_upload, name='consumer-committee-upload'),
    path('consumer-committee/generate-pdf/<int:serial_no>/<int:project_id>/', download_consumer_committee_pdf),
    path('preview-template/', preview_template),

]







# | Nepali Term              | English Equivalent      |
# | ------------------------ | ----------------------- |
# | कार्यक्रमको विवरण        | **Program Detail**      |
# | सुचारु प्रक्रिया         | **Initiation Process**  |
# | उपभोक्ता समिति           | **Consumer Committee**  |
# | लागत अनुमान              | **Budget Estimate**     |
# | योजना सम्झौता            | **Agreement**   |
# | संचालन स्थल              | **Operation Location**  |
# | किस्ता भुक्तानी सम्बन्धी | **Payment Installment** |
# | अन्य डकुमेन्ट            | **Documents**     |
