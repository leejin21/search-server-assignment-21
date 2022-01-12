"""
* 할 일
 - TODO 다 result 객체 반환하도록 처리

"""

from sqlalchemy import select

from .entities import db
from .entities import Company, CompanyName, Tag



def db_add(instance):
    db.session.add(instance)


def db_add_all(instances):
    db.session.add_all(instances)


def db_commit():
    db.session.commit()


class CompanyRepository:
    @staticmethod
    def init_instance():
        return Company()

    @staticmethod
    def search_by_name(name):
        stmt = select(Company).\
                join(Company.names).\
                filter(CompanyName.name == name)
        result = db.session.execute(stmt).fetchone()
        return result


class CompanyNameRepository:
    @staticmethod
    def init_instance(lang, name):
        return CompanyName(lang=lang, name=name)

    @staticmethod
    def search_by_name(name):
        stmt = select(CompanyName).where(CompanyName.name==name)
        result = db.session.execute(stmt).fetchone()
        return result
    
    @staticmethod
    def search_by_substring_front(substr):
        stmt = CompanyName.query.filter(CompanyName.name.like(substr+'%'))
        results = db.session.execute(stmt).all()
        return results
    
    @staticmethod
    def search_by_substring_middle(substr):
        stmt = CompanyName.query.filter(CompanyName.name.contains(substr))
        results = db.session.execute(stmt).all()
        return results


class TagRepository:
    @staticmethod
    def init_instance(lang, name):
        return Tag(lang=lang, name=name)
    
    @staticmethod
    def search_by_name(name):
        stmt = select(Tag).where(Tag.name==name)
        result = db.session.execute(stmt)
        tag = result.fetchone().Tag
        return tag
    
    @staticmethod
    def search_tags_by_company_name(lang, name):
        stmt = select(Tag).\
            join(Tag.companies).\
            join(Company.names).\
            filter(CompanyName.name==name)
            
        results = db.session.execute(stmt)
        return [{"name": row.name, "lang": row.lang} for row in results.scalars() if row.lang == lang]
        