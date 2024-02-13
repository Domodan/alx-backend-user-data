#!/usr/bin/env python3
"""
    Module: Basic authentication for the API
"""
import re
import base64
import binascii
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
        Basic Authentication Class
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """
            Extracts the Base64 part of the Authorization header
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            head_match = re.fullmatch(pattern, authorization_header.strip())
            if head_match is not None:
                return head_match.group('token')
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str,
            ) -> str:
        """
            Decodes a base64-encoded authorization header
        """
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str,
            ) -> Tuple[str, str]:
        """
            Extracts user credentials from a base64-decoded authorization
        """
        if type(decoded_base64_authorization_header) == str:
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')
                return user, password
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """
            Returns User Instance based on the authentication credentials
        """
        if email is None or not isinstance(email, str):
            return None

        if pwd is None or not isinstance(pwd, str):
            return None

        try:
            users = User.search({'email': email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(pwd):
                return user

        return None

    '''def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)'''
