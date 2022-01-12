from sqlalchemy import select

from .entities import db
from .entities import Companies, CompanyNames, Tags

def db_add(instance):
    db.session.add(instance)

def db_add_all(instances):
    db.session.add_all(instances)

def db_commit():
    db.session.commit()

class CompanyRepository:
    @staticmethod
    def init_instance():
        return Companies()

class CompanyNameRepository:
    @staticmethod
    def init_instance(lang, name):
        return CompanyNames(lang=lang, name=name)

class TagRepository:
    @staticmethod
    def init_instance(lang, name):
        return Tags(lang=lang, name=name)
    
    @staticmethod
    def search_by_name(name):
        stmt = select(Tags).where(Tags.name==name)
        result = db.session.execute(stmt)
        tag = result.fetchone().Tags
        return tag