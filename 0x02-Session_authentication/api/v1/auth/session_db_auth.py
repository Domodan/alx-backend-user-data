#!/usr/bin/env python3
"""
    Module: Session Authentication From Database
"""
from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
        Class: SessionDBAuth with Database for session Persistance
    """

    def create_session(self, user_id=None):
        """
        Create a Session ID for a user_id
        Args:
           user_id (str): user id
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        user = UserSession(user_id=user_id, session_id=session_id)
        user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns a user ID based on a session ID
        Args:
            session_id (str): session ID
        Return:
            user id or None if session_id is None or not a string
        """
        user_id = UserSession.search({"session_id": session_id})
        if user_id:
            return user_id
        return None

    def destroy_session(self, request=None):
        """
            Delete a UserSession instance based on Session ID
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_session = UserSession.search({"session_id": session_id})
        if user_session:
            user_session[0].remove()
            return True
        return False
