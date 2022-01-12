"""
* 앞으로 할 일
- TODO REFACTOR
    클래스 이름 전부 단수로 바꾸기
- TODO STUDY
    Companies에서 CompanyNames를 null=False로 갖게 되는 경우 어떻게 되는 지

"""

from ...repository import db

CompanyTags = db.Table('company_tags',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True),
    db.Column('tags_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Companies(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    names = db.relationship('CompanyNames', backref='Company', lazy=True)
    tags = db.relationship('Tags', secondary=CompanyTags, back_populates="companies")

class CompanyNames(db.Model):
    __tablename__ = 'companynames'
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    companies = db.relationship('Companies', secondary=CompanyTags, back_populates="tags")