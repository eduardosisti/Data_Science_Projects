from datetime import datetime
from sqlalchemy.dialects.postgresql import insert as pg_insert
from database.database import db


class BaseModel:
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.utcnow)

    @classmethod
    def one_or_none(cls, **kwargs):
        return cls.filter(**kwargs).one_or_none()

    @classmethod
    def filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs)

    @classmethod
    def get_or_create(cls, auto_flush=False, auto_commit=True, **kwargs):
        instance = cls.query.filter_by(**kwargs).first()

        if instance:
            return instance
        else:
            instance = cls.create(auto_flush, auto_commit, **kwargs)

            return instance

    @classmethod
    def create(cls, flush=False, commit=True, **kwargs):
            instance = cls(**kwargs)

            if commit:
                instance.save()

            if flush:
                instance.flush()

            return instance

    @classmethod
    def create_on_conflict(cls, unique_entry, ignore=True, update=False, **kwargs):
        insert_statement = pg_insert(cls).values(**kwargs)

        if ignore == update:
            raise Exception('Ignore and Update Flags Cannot Be The Same')

        if ignore:
            statement = insert_statement.on_conflict_do_nothing(index_elements=[unique_entry])

        elif update:
            statement = insert_statement.on_conflict_do_update(index_elements=unique_entry,
                                                               set_=dict(**kwargs))
        db.session.execute(statement)

    def set_values(self, data_dict):
        for key, value in data_dict.items():
            setattr(self, key, data_dict.get(key, getattr(self, key)))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def flush(self):
        db.session.add(self)
        db.session.flush()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, data_dict):
        self.set_values(data_dict)
        self.save()

        return self