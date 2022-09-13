
from sqlalchemy_utils import *
from sqlalchemy.orm import *
from sqlalchemy import *

#-----
#create_table('postgresql+psycopg2://wym_admin:admin@127.0.0.1:5431/wym_admin')
Base = declarative_base()

class User(Base):
     __tablename__ = "wym_admin"

     id = Column(Integer, primary_key=True)
     date = Column(String)
     name = Column(String)
     mail = Column(String)
     commentaire = Column(String)

     def __repr__(self):
         return f"User(id= {self.id!r}, date={self.date!r}, name={self.name!r}, mail={self.mail!r}, commentaire={self.commentaire!r})"

engine = create_engine('postgresql+psycopg2://wym_admin:admin@127.0.0.1:5431/wym_admin', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

user2 = User(id=1, date='12/09/22', commentaire='commentaire', mail='test@contact.org',name='Maxime')

session.add(user2)
session.commit()

# def connexion():
#	if database_exists('postgresql://postgres@localhost/name')==False: #si bdd existe pas on la créé
#		create_database('postgresql://postgres@localhost/name')
	
#	try:
#		database_exists('postgresql://postgres@localhost/name')
#	except:
#		print("erreur dans la création de la base")
	

# def check_bdd():
	
	
# def init_bdd():


# def check_tables():

