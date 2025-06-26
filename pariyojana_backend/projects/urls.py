# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from projects.views.project import ProjectViewSet
# # from projects.views.program_detail import ProgramDetailViewSet 
# from projects.views.initiation_process import InitiationProcessViewSet

# router = DefaultRouter()
# router.register(r'projects', ProjectViewSet, basename='project')
# # router.register(r'program-details', ProgramDetailViewSet, basename='program-detail')
# router.register(r'initiation-process', InitiationProcessViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
    
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects.views.project import ProjectViewSet
# from projects.views.program_detail import ProgramDetailViewSet 
from projects.views.initiation_process import InitiationProcessViewSet

from projects.views.consumer_committee import (
    ConsumerCommitteeListView,
    consumer_committee_upload,
    download_consumer_committee_letter,
)

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'initiation-process', InitiationProcessViewSet)
# router.register(r'program-details', ProgramDetailViewSet, basename='program-detail')
urlpatterns = [
    path('', include(router.urls)),

    # Add consumer committee urls here:
    path('consumer-committee/', ConsumerCommitteeListView.as_view(), name='consumer-committee-list'),
    path('consumer-committee/upload/', consumer_committee_upload, name='consumer-committee-upload'),
    path('consumer-committee/download/<int:serial_no>/', download_consumer_committee_letter, name='consumer-committee-download'),
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
