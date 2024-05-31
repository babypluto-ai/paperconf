from rest_framework import permissions

from linkers.models import EditorConference

class IsConferenceEditor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_authenticated:
            return EditorConference.objects.filter(user=request.user, conference=obj).exists()
        
        return False
