from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from projects.models.Cost_Estimate.map_cost_estimate import MapCostEstimate
from authentication.models import VerificationLog
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from authentication.models import VerificationLog
from .serializers import VerificationLogSerializer

class VerificationLogViewSet(viewsets.ModelViewSet):
    queryset = VerificationLog.objects.all()
    serializer_class = VerificationLogSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        
        # For checkers - show only their pending documents
        if hasattr(user, 'verification_checked'):
            return queryset.filter(
                checker=user,
                status='pending'
            )
        
        # For approvers - show only checked documents assigned to them
        elif hasattr(user, 'verification_approved'):
            return queryset.filter(
                approver=user,
                status='checked'
            )
            
        return queryset.none()  



# authentication/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def check_document(request, document_id):
    try:
        doc = MapCostEstimate.objects.get(id=document_id)
        if doc.checker != request.user:
            return Response(
                {"error": "You are not authorized to check this document"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        doc.status = 'checked'
        doc.save()
        
        VerificationLog.objects.create(
            project=doc.project,
            file_title=doc.title,
            status='checked',
            remarks=request.data.get('remarks', ''),
            checker=request.user,
            source_model='MapCostEstimate',
            source_id=doc.id,
            file_path=doc.file.url if doc.file else ""
        )
        
        return Response({"status": "checked"}, status=status.HTTP_200_OK)
    
    except MapCostEstimate.DoesNotExist:
        return Response(
            {"error": "Document not found"},
            status=status.HTTP_404_NOT_FOUND
        )

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_document(request, document_id):
    try:
        doc = MapCostEstimate.objects.get(id=document_id)
        if doc.approver != request.user:
            return Response(
                {"error": "You are not authorized to approve this document"},
                status=status.HTTP_403_FORBIDDEN
            )
        if doc.status != 'checked':
            return Response(
                {"error": "Document must be checked before approval"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        doc.status = 'approved'
        doc.is_verified = True
        doc.save()
        
        VerificationLog.objects.create(
            project=doc.project,
            file_title=doc.title,
            status='approved',
            remarks=request.data.get('remarks', ''),
            approver=request.user,
            source_model='MapCostEstimate',
            source_id=doc.id,
            file_path=doc.file.url if doc.file else ""
        )
        
        return Response({"status": "approved"}, status=status.HTTP_200_OK)
    
    except MapCostEstimate.DoesNotExist:
        return Response(
            {"error": "Document not found"},
            status=status.HTTP_404_NOT_FOUND
        )