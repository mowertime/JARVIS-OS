import json
from typing import Dict, Any, Optional, List
from datetime import datetime
from uuid import uuid4

class Session:
    def __init__(self, session_id: Optional[str] = None):
        self.session_id = session_id or str(uuid4())
        self.created_at = datetime.utcnow()
        self.history: List[Dict[str, Any]] = []
        self.context: Dict[str, Any] = {"device": "arch", "state": "idle"}
        self.metadata: Dict[str, Any] = {}
    
    def add_interaction(self, request: str, response: Dict[str, Any]):
        self.history.append({
            "timestamp": datetime.utcnow().isoformat(),
            "request": request,
            "response": response
        })
        self.context["state"] = "idle"
    
    def get_context(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "context": self.context,
            "history_count": len(self.history),
            "last_interaction": self.history[-1] if self.history else None
        }
    
    def clear_history(self):
        self.history = []
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "created_at": self.created_at.isoformat(),
            "history": self.history,
            "context": self.context,
            "metadata": self.metadata
        }

class SessionManager:
    def __init__(self):
        self.sessions: Dict[str, Session] = {}
    
    def create_session(self) -> Session:
        session = Session()
        self.sessions[session.session_id] = session
        return session
    
    def get_session(self, session_id: str) -> Optional[Session]:
        return self.sessions.get(session_id)
    
    def remove_session(self, session_id: str):
        self.sessions.pop(session_id, None)
    
    def cleanup_old(self, max_age_hours: int = 24):
        now = datetime.utcnow()
        expired = [
            sid for sid, session in self.sessions.items()
            if (now - session.created_at).total_seconds() > max_age_hours * 3600
        ]
        for sid in expired:
            self.remove_session(sid)
