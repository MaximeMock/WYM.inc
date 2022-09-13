
from sqlalchemy_utils import *
from sqlalchemy.orm import *
from sqlalchemy import *
from datetime import datetime 
#-----



class User(declarative_base()):
     __tablename__ = "wym_admin"

     _id = Column(Integer, primary_key=True)
     date = Column(String)
     name = Column(String)
     mail = Column(String)
     commentaire = Column(String)

     def __repr__(self):
         return f"User(id= {self._id!r}, date={self.date!r}, name={self.name!r}, mail={self.mail!r}, commentaire={self.commentaire!r})"

#engine = create_engine('postgresql+psycopg2://wym_admin:admin@127.0.0.1:5431/wym_admin', echo=True)
#Base.metadata.create_all(engine)
#Session = sessionmaker(bind=engine)
#session = Session()
#session.add(userX)
#session.commit()

class DB(port:str, log:str, password:str, nom_DB):

	def __init__(self, port='5432', log='wym_admin', password='admin', nom_DB='wym_admin'):
		self.port =port
		self.log =log 
		self.password =password
		self.nom_DB =nom_DB
		self.path = f'postgresql+psycopg2://{log}:{password}@127.0.0.1:{port}/{nom_DB}'
		self.engine = False
	
 	def create_connection(self):
 		self.engine = create_engine(path, echo=True)
 		return self.engine

	def check_bdd(self):
		try:
			self.engine
			return engine
		except:
			return False
		
	def check_tables(self):
		return inspect(self.connection).has_table(self.nom_DB)

		
	def init_bdd(self):
		if self.engine == False:
			create_database(path)
		
		if self.check_tables(self.engine)==False:
			Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		session = Session()

	def recup_user(self, _id, comme, mail, name):
		now = datetime.now()
		current_time = now.strftime("%Y/%m/%d %H:%M:%S")
		Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		session = Session()
		userX= User(_id=_id, date=current_time, name=name, mail=mail, commentaire=comm)
		session.add(userX)
		session.commit()
		return userX
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
