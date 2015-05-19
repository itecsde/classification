from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase
from sqlalchemy.orm import relationship

BaseSDE2 = declarative_base()

class Taggable(AbstractConcreteBase, BaseSDE2):
    id = Column(Integer, primary_key=True)


class ReutersNewItem(Taggable):
    __tablename__ = 'reuters_new_items'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    __mapper_args__ = {'polymorphic_identity': 'ReutersNewItem',"concrete": True}      
    name = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    topics = Column(String(255), nullable=True)
    cgisplit = Column(String(255), nullable=True)


class Tag(BaseSDE2):
    __tablename__ = 'tags'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

class TaggableTagAnnotation(BaseSDE2):
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
    weight = Column(Float, nullable=False)
    type_tag = Column(String(255), nullable = False)
    wikipedia_article_id = Column(Integer, nullable = False)
    expanded = Column(Boolean, default=False)
    relatedness = Column(Float, nullable=True)
    expanded_from = Column(Integer, nullable=True)