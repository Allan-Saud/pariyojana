from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views.project import ProjectViewSet
from projects.views.Initiation_Process.initiation_process import InitiationProcessViewSet
from projects.views.Program_Details.program_detail import ProgramDetailViewSet
from projects.views.Program_Details.beneficiary_details import BeneficiaryDetailViewSet
from projects.views.Consumer_Committee.consumer_committee_details import ConsumerCommitteeDetailViewSet
from projects.views.Consumer_Committee.monitoring_facilitation_committee import MonitoringFacilitationCommitteeViewSet
from projects.views.Cost_Estimate.cost_estimate_detail import CostEstimateDetailViewSet
from projects.views.Consumer_Committee.consumer_committee import (
    ConsumerCommitteeListView,
    consumer_committee_upload,
    download_consumer_committee_pdf,
)
from projects.views.Consumer_Committee.consumer_committee import preview_template
from projects.views.Project_Aggrement.project_aggrement_details import ProjectAgreementDetailsViewSet
from projects.views.Consumer_Committee.official_detail import OfficialDetailViewSet
from projects.views.Operation_Location.operation_location import OperationSitePhotoViewSet
from projects.views.Installment_Payment.bank_details import BankDetailViewSet
from projects.views.Installment_Payment.payment_related_details import PaymentRelatedDetailViewSet
from projects.views.Installment_Payment.bankaccount_recommendation import BankAccountRecommendationViewSet
from projects.views.Installment_Payment.account_photos import AccountPhotoViewSet
from projects.views.Cost_Estimate.map_cost_estimate import MapCostEstimateViewSet
from projects.views.ExtendedDeadline.extended_deadline import ExtendedDeadlineViewSet
from projects.views.Cost_Estimate.cost_estimate_revision import CostEstimateRevisionViewSet
from projects.views.progress_stage import ProjectProgressViewSet

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
router.register(r'bank-details', BankDetailViewSet, basename='bank-detail')
router.register(r'payment-details', PaymentRelatedDetailViewSet)
router.register(r'bank-account-recommendation', BankAccountRecommendationViewSet, basename='bank-recommendation')
router.register(r'account-photos', AccountPhotoViewSet, basename='account-photos')
router.register(r'map-cost-estimate', MapCostEstimateViewSet)
router.register(r'extended-deadlines', ExtendedDeadlineViewSet, basename='extended-deadline')
router.register(r'cost-estimate-revisions', CostEstimateRevisionViewSet, basename='cost-estimate-revision')
router.register(r'project-progress', ProjectProgressViewSet, basename='project-progress')

urlpatterns = [
    path('', include(router.urls)),


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
