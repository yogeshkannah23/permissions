from rest_framework.permissions import BasePermission,SAFE_METHODS



class IsOwnerOrViewOnly(BasePermission):
    def has_permission(self, request, view):
        print(view)
        return request.method in SAFE_METHODS
    
    