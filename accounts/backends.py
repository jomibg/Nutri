from django.contrib.auth.models import User

class EmailAuth(object):
    def authenticate(self, request, username=None, password=None):
        try:
            u=User.objects.get(email=username)
            if u.check_password(password):
                return u
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


