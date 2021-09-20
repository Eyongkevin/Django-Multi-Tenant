# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate
# from django.forms import ValidationError
# from typing import Dict, Any 


# class CustomLoginForm(AuthenticationForm):
#     # def clean(self) -> Dict[str, Any]:
#     #     return super().clean()
#     def clean(self):
#         userid = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')
        
#         if userid and password:
#             #the backends will be picked from the settings from the variable named AUTHENTICATION_BACKENDS
#             #and the authentication method of each of one will be called in the same order as the order in the AUTHENTICATION_BACKENDS list
#             self.user_cache = authenticate(
#                 username=userid, 
#                 password=password
#             )
#             import pdb;pdb.set_trace()
#             if self.user_cache is None:
#                 raise ValidationError(
#                     self.error_messages['invalid_login'],
#                     code='invalid_login',
#                     params={'username': self.username_field.verbose_name},
#                 )
#             else:
#                 self.confirm_login_allowed(self.user_cache)
        
#         return self.cleaned_data