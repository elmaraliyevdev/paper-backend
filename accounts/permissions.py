from rest_framework.permissions import BasePermission


class IsAuthenticatedOwner(BasePermission):
    def has_permission(self, request, view):
        # work when your access /item/
        if request.user and request.user.is_authenticated:
            if request.user.id in [1, 2, 3]:
                return True
            else:
                return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # work when your access /item/item_id/
        # Instance must have an attribute named `owner`.
        return obj.user == request.user
