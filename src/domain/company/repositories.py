"""
* 할 일
 - TODO 다 result 객체 반환하도록 처리

"""

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

    @staticmethod
    def search_by_name(name):
        stmt = select(Companies).\
                join(Companies.names).\
                filter(CompanyNames.name == name)
        result = db.session.execute(stmt).fetchone()
        return result

class CompanyNameRepository:
    @staticmethod
    def init_instance(lang, name):
        return CompanyNames(lang=lang, name=name)

    @staticmethod
    def search_by_name(name):
        stmt = select(CompanyNames).where(CompanyNames.name==name)
        result = db.session.execute(stmt).fetchone()
        return result
    
    @staticmethod
    def search_by_substring_front(substr):
        stmt = CompanyNames.query.filter(CompanyNames.name.like(substr+'%'))
        results = db.session.execute(stmt).all()
        return results
    
    @staticmethod
    def search_by_substring_middle(substr):
        stmt = CompanyNames.query.filter(CompanyNames.name.contains(substr))
        results = db.session.execute(stmt).all()
        return results

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
    
    @staticmethod
    def search_tags_by_company_name(lang, name):
        stmt = select(Tags).\
            join(Tags.companies).\
            join(Companies.names).\
            filter(CompanyNames.name==name)
            
        results = db.session.execute(stmt)
        return [{"name": row.name, "lang": row.lang} for row in results.scalars() if row.lang == lang]
        