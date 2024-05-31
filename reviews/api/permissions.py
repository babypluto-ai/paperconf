from django.shortcuts import get_object_or_404
from rest_framework import permissions

from papers.models import Paper
from linkers.models import ReviewerPaper

class IsReviewerOrPaperOwner(permissions.BasePermission):
    """
    Custom permission to allow only reviewers or paper owners to view the reviews.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.paper.user == request.user or obj.user == request.user

class IsReviewOwner(permissions.BasePermission):
    """
    Custom permission to allow only the review owner to perform actions on the review.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class CanSubmitReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if 'pk' in view.kwargs:
            paper = get_object_or_404(Paper, pk=view.kwargs['pk'])
            user = request.user
            # Check if the user is assigned to review the paper
            if ReviewerPaper.objects.filter(paper=paper, user=user).exists():
                return True
        return False