#!/usr/bin/env python3
"""
    Module: User Session Databases Storage
"""
from models.base import Base


class UserSession(Base):
    """
        Class: UserSession manages DB related session ids
    """

    def __init__(self, *args: list, **kwargs: dict):
        """
            Initializes a User session instance
        """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
