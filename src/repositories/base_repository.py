# src/repositories/base_repository.py
from typing import Any, Dict, List, Optional
from src.models import db

class BaseRepository:
    model = None

    def __init__(self):
        if self.model is None:
            raise NotImplementedError("La subclase debe definir 'model'")

    def create(self, **kwargs) -> Any:
        instance = self.model(**kwargs)
        try:
            db.session.add(instance)
            db.session.commit()
            return instance
        except Exception:
            db.session.rollback()
            raise

    def get_by_id(self, _id: int) -> Optional[Any]:
        return self.model.query.get(_id)

    def get_all(self, filters: Dict = None) -> List[Any]:
        q = self.model.query
        if filters:
            q = q.filter_by(**filters)
        return q.all()

    def update(self, _id: int, **kwargs) -> Optional[Any]:
        obj = self.get_by_id(_id)
        if not obj:
            return None
        try:
            for k, v in kwargs.items():
                if hasattr(obj, k):
                    setattr(obj, k, v)
            db.session.commit()
            return obj
        except Exception:
            db.session.rollback()
            raise

    def delete(self, _id: int) -> bool:
        obj = self.get_by_id(_id)
        if not obj:
            return False
        try:
            db.session.delete(obj)
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            raise
