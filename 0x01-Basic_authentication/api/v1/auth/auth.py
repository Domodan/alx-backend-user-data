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
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith(''):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True

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
