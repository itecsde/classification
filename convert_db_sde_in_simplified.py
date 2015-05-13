import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.engine import url
from sqlalchemy.orm import sessionmaker
from db_simplified_declarative import Base, Document, Annotation
from db_sde_declarative import BaseSDE, Report, TaggableTagAnnotation,Tag
from db_sde_declarative2 import BaseSDE2, ReutersNewItem, TaggableTagAnnotation,Tag



def get_original_category(scraped_from):          
    if "healthNews" in scraped_from:
        cat = "Health"
    elif "artsNews" in scraped_from:
        cat = "Art"
    elif "politicsNews" in scraped_from:
        cat = "Politics"
    elif "sportsNews" in scraped_from:
        cat = "Sport"
    elif "scienceNews" in scraped_from:
        cat = "Science"
    elif "technologyNews" in scraped_from:
        cat = "Technology"
    elif "GCA-Economy2010" in scraped_from:
        cat = "Economy"
    elif "businessNews" in scraped_from:
        cat = "Business"   
    else:
        #Los de la categoria Fashion no los vamos a tener en cuenta 
        cat = ""
    return cat                                       





corpus_databases = ["corpus_reuters_27000_threshold_01","corpus_reuters_27000_annotated_with_title_and_description_01","corpus_ohsumed_threshold_01","corpus_ohsumed_th_01_expanded","corpus_20_newsgroups_threshould_01","corpus_20_newsgroups_th_01_expanded","corpus_ieee_threshould_01","corpus_ieee_th_01_expanded","corpus_merlot_threshold_01","corpus_ohsumed_multilabel_threshold_01", "corpus_uvigomed_multilabel_threshold_01","corpus_uvigomed_threshold_01","corpus_ohsumed_randomized_threshold_01","corpus_ohsumed_randomized_multilabel_threshold_01","corpus_reuters_rcv2_threshold_01","corpus_reuters_rcv1_threshold_01","corpus_reuters_rcv2_translated_to_english_google_translate","corpus_wikipedia_english_threshold_01","corpus_wikipedia_spanish_annotations_translated_to_en_th_01"]

simplified_databases = []
for corpus_db in corpus_databases:    
    simplified_databases.append(corpus_db.replace("corpus", "simplified"))
    
###################################################################################  
#### Aqui es donde escogemos la base de datos de corpus_databases a simplificar ###
###################################################################################
#############
selection = 18
#############

corpus_db = corpus_databases[selection]
simplified_db = simplified_databases[selection]

## Conversiones de datos
txt_url_db_corpus = str('mysql://classify_user:classify_password@localhost/' + corpus_db)
txt_url_db_simplified = str('mysql://classify_user:classify_password@localhost/' + simplified_db)
url_db_corpus = url.make_url(txt_url_db_corpus)
url_db_simplified = url.make_url(txt_url_db_simplified)


engine_db_sde = create_engine(url_db_corpus)
engine_db_classify = create_engine(url_db_simplified)


Base.metadata.bind = engine_db_classify
if selection in [0,1]:
    BaseSDE.metadata.bind = engine_db_sde
else:
    BaseSDE2.metadata.bind = engine_db_sde
 
DBClassifySession = sessionmaker(bind=engine_db_classify)
DBSDESession = sessionmaker(bind=engine_db_sde)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session_classify = DBClassifySession()
session_sde = DBSDESession()


#### CASO REUTERS ya que aun en tabla reports
if selection in [0,1]:
    for report in session_sde.query(Report).all():
        original_cat = get_original_category(report.scraped_from)
        if original_cat != "":        
            new_document = Document(name = report.name, description = report.description, original_category = original_cat)
            session_classify.add(new_document)
            session_classify.commit()
            
            for taggable_tag_annotation in session_sde.query(TaggableTagAnnotation).filter(TaggableTagAnnotation.taggable_type == "Report", TaggableTagAnnotation.taggable_id == report.id):
                new_annotation = Annotation(name = taggable_tag_annotation.tag.name, weight = taggable_tag_annotation.weight, document = new_document)
                session_classify.add(new_annotation)        
            print report.name
            session_classify.commit()
            print "--"

#### RESTO de CASOS. Ya en tabla ReutersNewItem            
else:
    for report in session_sde.query(ReutersNewItem).all():
        original_cat = report.topics
        if report.cgisplit != None:
            if "train" in report.cgisplit:
                cgisplit = "train"
            elif "test" in report.cgisplit:
                cgisplit = "test"
        else:
            cgisplit = None

        if original_cat != "":        
            new_document = Document(name = report.name, description = report.description, original_category = original_cat, cgisplit = cgisplit)
            session_classify.add(new_document)
            session_classify.commit()
            
            for taggable_tag_annotation in session_sde.query(TaggableTagAnnotation).filter(TaggableTagAnnotation.taggable_type == "ReutersNewItem", TaggableTagAnnotation.type_tag == "automatic", TaggableTagAnnotation.taggable_id == report.id):                
                new_annotation = Annotation(name = taggable_tag_annotation.tag.name, weight = taggable_tag_annotation.weight, document = new_document, expanded = taggable_tag_annotation.expanded, relatedness = taggable_tag_annotation.relatedness, expanded_from = taggable_tag_annotation.expanded_from, old_id = taggable_tag_annotation.id)
                session_classify.add(new_annotation)        
            print report.name
            session_classify.commit()
            print "--"


