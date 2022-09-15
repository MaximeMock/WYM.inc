from sqlalchemy_utils import *
from sqlalchemy.orm import *
from sqlalchemy import *
from datetime import datetime 

#-----

Base = declarative_base()

class Stats(Base):
    __tablename__ = 'statistics'

    id_stat = Column(Integer, primary_key=True) # autoincrements by default
    date = Column(DateTime, default=datetime.utcnow)
    
    text_input = Column(String)
    text_output = Column(String)
    
    nb_mot_E = Column(Integer)
    frq_mot_E = Column(Integer)
    nb_carac_E = Column(Integer)
    
    nb_mot_S = Column(Integer)
    frq_mot_S = Column(Integer)
    nb_carac_S = Column(Integer)
    
    diff_mot = Column(Integer)
    diff_carac = Column(Integer)
    
    def __repr__(self):
    	return f"Stats(id_stat = {self._id!r}, date={self.date!r}, text_input={self.text_input!r}, text_output={self.text_output!r}, nb_mot_E={self.nb_mot_E!r}, frq_mot_E={self.frq_mot_E!r}, nb_carac_E={self.nb_carac_E!r}, nb_mot_S={self.nb_mot_S!r}, frq_mot_S={self.frq_mot_S!r}, nb_carac_S={self.nb_carac_S!r}, diff_mot={self.diff_mot!r}, diff_carac={self.diff_carac!r}"
#-----		
		
class DB_stats:#(port:str, log:str, password:str, nom_DB:str):

#connexion et verification

	def __init__(self, port='5432', log='wym_admin', password='admin', nom_DB='wym_stats'):
		self.port = port
		self.log = log 
		self.password = password
		self.nom_DB = nom_DB
		self.path = f'postgresql+psycopg2://{log}:{password}@0.0.0.0:{port}/{nom_DB}'
		self.engine = False
	
	def create_connection(self):
		self.engine = create_engine(self.path, echo=True)
		return self.engine

	def check_bdd(self):
		try:
			self.engine
			return self.engine
		except:
			return False

	def check_tables(self):
		return inspect(self.engine).has_table(self.nom_DB)

	def init_bdd(self):
		if self.engine == False:
			create_database(self.path)

		if self.check_tables()==False:
			Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		session = Session()
		return session

#génération

	def recup_stats(self, text_input, text_output, nb_mot_E, frq_mot_E, nb_carac_E, nb_mot_S, frq_mot_S, nb_carac_S, diff_mot, diff_carac):
		
		Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		session = Session()
	
		stats_id = session.query(Stats._id).count()+1
		now = datetime.now()
		current_time = now.strftime("%Y/%m/%d %H:%M:%S")
		
		statX = Stats(id_stat = stats_id, date=current_time, text_input=text_input, text_output=text_output, nb_mot_E=nb_mot_E, frq_mot_E=frq_mot_E, nb_carac_E=nb_carac_E, nb_mot_S=nb_mot_S, frq_mot_S=frq_mot_S, nb_carac_S=nb_carac_S, diff_mot = diff_mot, diff_carac = diff_carac) 
		
		session.add(statX)
		session.commit()
		
		return statX		
		
		
	
		
		
			
