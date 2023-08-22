'''
Copyright 2023 Sebastian Feiert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
__author__ = 'Sebastian Feiert'

class PasswordContainer:
    def __init__(self,):

        self.pw_id = 1
        
        self.request_password = 'Password_A'
        self.license_password = 'Password_B'
        self.user_db_password = 'Password_C'
        self.settings_db_password = 'Password_D'

    def get_request_password(self):
        return(self.request_password)
    
    def get_license_password(self):
        return(self.license_password)
    
    def get_db_user_password(self):
        return(self.user_db_password)
    
    def get_db_settings_password(self):
        return(self.settings_db_password)
    
    def get_passwort_id(self):
        return(self.pw_id)