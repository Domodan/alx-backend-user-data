#!/usr/bin/env python3
"""
    Module: API Authentication
"""
from flask import request
from typing import List, TypeVar
import fnmatch


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
