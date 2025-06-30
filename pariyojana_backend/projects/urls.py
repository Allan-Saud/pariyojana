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
from projects.views.Project_Aggrement.project_plan_tracker import (
    ProjectPlanTrackerListView, upload_project_plan_tracker, download_project_plan_tracker_pdf
)
from projects.views.Project_Aggrement.project_aggrement_workorder import (
    ProjectAgreementWorkorderListView,
    project_agreement_workorder_upload,
    download_project_agreement_workorder_pdf,
)

from projects.views.Documents.other_document import OtherDocumentListView, download_other_document_pdf,preview_other_document_template


    


from projects.views.Consumer_Committee.consumer_committee import preview_template
from projects.views.Project_Aggrement.project_plan_tracker import preview_project_plan_tracker_template
from projects.views.Project_Aggrement.project_aggrement_workorder import preview_project_aggrement_workorder_template
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
from projects.views.Documents.documents import DocumentViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'initiation-process', InitiationProcessViewSet)
router.register(r'program-details', ProgramDetailViewSet, basename='program-detail')
router.register(r'beneficiaries', BeneficiaryDetailViewSet, basename='beneficiaries')
router.register(r'consumer-committee-details', ConsumerCommitteeDetailViewSet, basename='consumer-committee-detail')
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
router.register(r'documents', DocumentViewSet, basename='document')
urlpatterns = [
    path('', include(router.urls)),


    path('consumer-committee/', ConsumerCommitteeListView.as_view(), name='consumer-committee-list'),
    path('consumer-committee/upload/', consumer_committee_upload, name='consumer-committee-upload'),
    path('consumer-committee/generate-pdf/<int:serial_no>/<int:project_id>/', download_consumer_committee_pdf),
    path('consumer-committee/preview-template/<int:serial_no>/<int:project_id>/', preview_template, name='preview-template'),
     
    path('project-plan-tracker/', ProjectPlanTrackerListView.as_view()),
    path('project-plan-tracker/upload/', upload_project_plan_tracker),
    path('project-plan-tracker/download/<int:serial_no>/<int:project_id>/', download_project_plan_tracker_pdf),
    path('plan_aggrement/preview-template/<int:serial_no>/<int:project_id>/', preview_project_plan_tracker_template, name='project-plan-tracker-preview-template'),
    
    
    path('project-aggrement/', ProjectAgreementWorkorderListView.as_view(), name='project_agreement_list'),
    path('project-aggrement/upload/', project_agreement_workorder_upload, name='project_agreement_upload'),
    path('project-aggrement/download/<int:serial_no>/<int:project_id>/', download_project_agreement_workorder_pdf, name='project_agreement_pdf_download'),
    path('project_aggrement_workorder/preview-template/<int:serial_no>/<int:project_id>/', preview_project_aggrement_workorder_template, name='project-plan-tracker-preview-template'),
    
    
    path('other-documents/<int:project_id>/', OtherDocumentListView.as_view(), name='other-documents-list'),
    path('other-documents/download/<int:serial_no>/<int:project_id>/', download_other_document_pdf, name='other-document-download'),
    path('other-documents/preview-template/<int:serial_no>/<int:project_id>/', preview_other_document_template, name='other-document-preview-template'),
    
    

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
