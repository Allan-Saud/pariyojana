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
from projects.views.Installment_Payment.first_installment import (
    FirstInstallmentListView,
    upload_first_installment_file,
    download_first_installment_file,
    download_first_installment_pdf,
    preview_first_installment_template
)
from projects.views.Installment_Payment.second_installment import (
    SecondInstallmentListView,
    second_installment_upload,
    download_second_installment_pdf,
    preview_template as preview_second_installment_template,
)
from projects.views.Installment_Payment.third_installment import (
    ThirdInstallmentListView,
    third_installment_upload,
    download_third_installment_pdf,
    preview_template as preview_third_installment_template,
)
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
from projects.views.Cost_Estimate.cost_estimate_detail import generate_bill_pdf
from projects.views.Installment_Payment.payment_related_details import generate_payment_bill_pdf



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
    path('project_aggrement_workorder/preview-template/<int:serial_no>/<int:project_id>/', preview_project_aggrement_workorder_template, name='project-aggrement-workorder-preview-template'),
    
    
    path('other-documents/<int:project_id>/', OtherDocumentListView.as_view(), name='other-documents-list'),
    path('other-documents/download/<int:serial_no>/<int:project_id>/', download_other_document_pdf, name='other-document-download'),
    path('other-documents/preview-template/<int:serial_no>/<int:project_id>/', preview_other_document_template, name='other-document-preview-template'),
    
    path('first-installment/', FirstInstallmentListView.as_view(), name='first-installment-list'),
    path('first-installment/upload/', upload_first_installment_file, name='first-installment-upload'),
    path('first-installment/download-file/<int:serial_no>/', download_first_installment_file, name='first-installment-download-file'),
    path('first-installment/generate-pdf/<int:serial_no>/<int:project_id>/', download_first_installment_pdf, name='first-installment-generate-pdf'),
    path(
    'first-installment/preview-template/<int:serial_no>/<int:project_id>/',
    preview_first_installment_template,
    name='first-installment-preview-template'
    ),
    
    
    path('second-installment/<int:project_id>/', SecondInstallmentListView.as_view(), name='second-installment-list'),
    path('second-installment/<int:project_id>/upload/', second_installment_upload, name='second-installment-upload'),
    path('second-installment/generate-pdf/<int:serial_no>/<int:project_id>/', download_second_installment_pdf, name='download-second-installment-pdf'),
    path('second-installment/preview-template/<int:serial_no>/<int:project_id>/', preview_second_installment_template, name='preview-second-installment-template'),
    
    
    
    path('third-installment/<int:project_id>/', ThirdInstallmentListView.as_view(), name='third-installment-list'),
    path('third-installment/<int:project_id>/upload/', third_installment_upload, name='third-installment-upload'),
    path('third-installment/generate-pdf/<int:serial_no>/<int:project_id>/', download_third_installment_pdf, name='download-third-installment-pdf'),
    path('third-installment/preview-template/<int:serial_no>/<int:project_id>/', preview_third_installment_template, name='preview-third-installment-template'),
    
    
    path('bill/project/<int:project_id>/pdf/', generate_bill_pdf, name='generate-bill-pdf'),
    
   

    path('installment/payment/project/<int:project_id>/pdf/', generate_payment_bill_pdf, name='generate-payment-bill-pdf'),


    
    
    # Nested project-specific endpoints (without affecting the DefaultRouter)

    path(
    '<int:serial_number>/beneficiaries/',
    BeneficiaryDetailViewSet.as_view({'get': 'list', 'post': 'create','patch': 'bulk_update'}),
    name='project-beneficiaries'
    ),


    path(
        '<int:serial_number>/initiation-process/',
        InitiationProcessViewSet.as_view({'get': 'list'}),
        name='project-initiation-process'
    ),

    path(
        '<int:serial_number>/program-details/',
        ProgramDetailViewSet.as_view({'get': 'list'}),
        name='project-program-details'
    ),

    path(
        '<int:serial_number>/consumer-committee-details/',
        ConsumerCommitteeDetailViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='project-consumer-committee-details'
    ),

    path(
        '<int:serial_number>/monitoring-committee/',
        MonitoringFacilitationCommitteeViewSet.as_view({'get': 'list'}),
        name='project-monitoring-committee'
    ),

    path(
        '<int:serial_number>/cost-estimate-details/',
        CostEstimateDetailViewSet.as_view({'get': 'list', 'post': 'create','patch': 'bulk_update'}),
        name='project-cost-estimate-details'
    ),

    path(
        '<int:serial_number>/official-details/',
        OfficialDetailViewSet.as_view({'get': 'list'}),
        name='project-official-details'
    ),

    path(
        '<int:serial_number>/documents/',
        DocumentViewSet.as_view({'get': 'list'}),
        name='project-documents'
    ),
    
    

    path(
        '<int:serial_number>/project-agreement-details/',
        ProjectAgreementDetailsViewSet.as_view({'get': 'list', 'post': 'create','patch': 'partial_update'}),
        name='project-agreement-details'
    ),
    
    
    path(
    '<int:serial_number>/project-agreement-details/<int:pk>/',
    ProjectAgreementDetailsViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'put': 'update',
        'delete': 'destroy',
    }),
    name='project-agreement-detail'
),

    path(
        '<int:serial_number>/operation-site-photos/',
        OperationSitePhotoViewSet.as_view({'get': 'list'}),
        name='project-operation-site-photos'
    ),

    
    
        path(
            '<int:serial_number>/bank-details/',
            BankDetailViewSet.as_view({'get': 'list', 'post': 'create'}),
            name='bank-details-list'
        ),
        path(
            '<int:serial_number>/bank-details/<int:pk>/',
            BankDetailViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'put': 'update', 'delete': 'destroy'}),
            name='bank-detail-detail'
    ),



    path(
        '<int:serial_number>/bank-account-recommendation/',
        BankAccountRecommendationViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='bank-account-recommendation-list'
    ),
    path(
        '<int:serial_number>/bank-account-recommendation/<int:pk>/',
        BankAccountRecommendationViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'put': 'update',
            'delete': 'destroy',
        }),
        name='bank-account-recommendation-detail'
    ),
    


    path(
    '<int:serial_number>/account-photos/',
    AccountPhotoViewSet.as_view({'get': 'list', 'post': 'create'}),
    name='project-account-photos'
),






    

    

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
