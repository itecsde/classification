import platform

from sqlalchemy import Column, ForeignKey, Integer, String, Float, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
 
class Document(Base):
    __tablename__ = 'documents'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }  
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), default = True)
    description = Column(Text, default = True)
    cgisplit = Column(String(255), nullable=True)
    original_category =  Column(Text, nullable=True)    
    classified_in_category_oercommons =  Column(String(255), nullable=True)
    classified_in_category_merlot =  Column(String(255), nullable=True)
    classified_in_category_cnx =  Column(String(255), nullable=True)
    classified_in_category_wikipedia =  Column(String(255), nullable=True)

    url =  Column(String(255), nullable=True)
    image_url =  Column(String(255), nullable=True)
    annotations = relationship("Annotation", backref="documents")
    evaluations = relationship("Evaluation", backref="documents")
 
class Annotation(Base):
    __tablename__ = 'annotations'
    __table_args__ = {  
        'mysql_engine': 'InnoDB',  
        'mysql_charset': 'utf8'  
    }
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    weight = Column(Float, nullable=True)
    weight_ponderate = Column(Float, nullable = True)
    document_id = Column(Integer, ForeignKey('documents.id'))   
    document = relationship(Document)
    expanded = Column(Boolean, default=False)
    relatedness = Column(Float, nullable=True)
    expanded_from = Column(Integer, nullable=True)
    old_id = Column(Integer, nullable = True)

class Evaluation(Base):
    __tablename__ = 'evaluations'
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey('documents.id'))
    evaluation = Column(String(250), nullable=True)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.

if platform.node() == "jumbo":
    engine = create_engine('mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_threshold_01?charset=utf8')
elif platform.node() == "babar":
    engine = create_engine('mysql://classify_user:classify_password@192.168.1.12/simplified_20newsgroups_threshold_01?charset=utf8')
elif platform.node() == "ganesha":
    engine = create_engine('mysql://classify_user:classify_password@192.168.1.12/simplified_20newsgroups_threshold_01?charset=utf8')
elif platform.node() == "dumbo":
    engine = create_engine('mysql://classify_user:classify_password@192.168.1.12/simplified_reuters_21578_threshold_01?charset=utf8')
elif platform.node() == "tantor":
    engine = create_engine('mysql://classify_user:classify_password@192.168.1.12/simplified_ohsumed_randomized_multilabel_threshold_01?charset=utf8')
elif platform.node() == "marcos-B85M-D3V":
    engine = create_engine('mysql://classify_user:classify_password@localhost/simplified_oercommons_threshold_01?charset=utf8')

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)