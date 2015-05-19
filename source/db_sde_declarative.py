from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase
from sqlalchemy.orm import relationship

BaseSDE = declarative_base()

class Taggable(AbstractConcreteBase, BaseSDE):
    id = Column(Integer, primary_key=True)

class Report(Taggable):
    __tablename__ = 'reports'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    __mapper_args__ = {'polymorphic_identity': 'Report',"concrete": True}  
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.    
    name = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    scraped_from = Column(String(255), nullable=True)        
    #tag = relationship("Tag", secondary=lambda: taggable_tag_annotations)    
    #tags = association_proxy('tag','tags')


class Tag(BaseSDE):
    __tablename__ = 'tags'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    #taggable = relationship("Taggable", secondary=lambda: taggable_tag_annotations)    
    #taggables = association_proxy('taggable')

class TaggableTagAnnotation(BaseSDE):
    __tablename__ = 'taggable_tag_annotations'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    
    id = Column(Integer, primary_key=True)
    taggable_id = Column(Integer, nullable = False)
    taggable_type = Column(String(255),nullable = False)
    tag_id = Column(Integer, ForeignKey('tags.id'))  
    tag = relationship(Tag)
    weight = Column(Float, nullable=True)
    type_tag = Column(String(255), nullable = True)
    wikipedia_article_id = Column(Integer, nullable = True)