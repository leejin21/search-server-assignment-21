from ...repository import db

class Companies(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    company_names = db.relationship('CompanyNames', backref='Company', lazy=True)

class CompanyNames(db.Model):
    __tablename__ = 'companynames'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)

class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)

CompanyTags = db.Table('company_tags',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True),
    db.Column('tags_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)