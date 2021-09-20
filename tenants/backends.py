# from tenants.utils import set_tenant_schema
# from django.conf import Settings
# from django.contrib.auth.models import User
# from django.utils.translation import gettext as _
# from django import forms 
# from django.contrib.auth.backends import ModelBackend

# def my_portal_authenticate(username, password):
#     if username == 'fooDjango' and password == 'barDjango':
#         return True 
#     return False

# class MyPortalBackend(ModelBackend):
#     def authenticate(self, request, **kwargs):
#         #import pdb;pdb.set_trace()
#         #set_tenant_schema('thor')
#         try:
#             username = kwargs['username']
#             password = kwargs['password']

#             user = User.objects.get(username=username)
#         except KeyError:
#             raise forms.ValidationError(
#                 _("Programming Error")
#             )
#         except User.DoesNotExist:
#             user = User(username=username)

#             user.is_staff = True
#             user.is_active = True 
#             user.save()
#         return user
    
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

