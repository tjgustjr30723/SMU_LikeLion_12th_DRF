from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    사용자가 객체의 소유자이거나 읽기 전용 요청인 경우에만 액세스를 허용하는 커스텀 퍼미션.
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 허용됩니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 객체의 소유자에게만 허용됩니다.
        return obj.user == request.user