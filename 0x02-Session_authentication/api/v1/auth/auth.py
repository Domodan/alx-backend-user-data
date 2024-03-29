#!/usr/bin/env python3
"""
    Module: API Authentication
"""
from flask import request
from typing import List, TypeVar
import os
import re


class Auth:
    """
        Manages API Authentication class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Method to check if auth is required
        """
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if exclusion_path[-1] == '*':
                    pattern = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    pattern = '{}/*'.format(exclusion_path[0:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
            Method to get authorization header
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            Method to get user from request
        """
        return None

    def session_cookie(self, request=None):
        """
            Returns a cookie from a request
        """
        if request is None:
            return None
        cookie_name = os.getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
