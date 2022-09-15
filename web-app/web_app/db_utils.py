from sqlalchemy_utils import *
from sqlalchemy.orm import *
from sqlalchemy import *
from datetime import datetime 
#-----

Base = declarative_base()

class User(Base):
     __tablename__ = "wym_admin"

     _id = Column(Integer, primary_key=True)
     date = Column(String)
     name = Column(String)
     mail = Column(String)
     commentaire = Column(String)

     def __repr__(self):
         return f"User(id= {self._id!r}, date={self.date!r}, name={self.name!r}, mail={self.mail!r}, commentaire={self.commentaire!r})"

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
    
#engine = create_engine('postgresql+psycopg2://wym_admin:admin@127.0.0.1:5431/wym_admin', echo=True)
#Base.metadata.create_all(engine)
#Session = sessionmaker(bind=engine)
#session = Session()
#session.add(userX)
#session.commit()

class DB:#(port:str, log:str, password:str, nom_DB):

	def __init__(self, port='5432', log='wym_admin', password='admin', nom_DB='wym_admin'):
		self.port =port
		self.log =log 
		self.password =password
		self.nom_DB =nom_DB
		self.path = f'postgresql+psycopg2://{log}:{password}@BDD:{port}/{nom_DB}'
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

	def recup_user(self, comme, mail, name):
		now = datetime.now()
		current_time = now.strftime("%Y/%m/%d %H:%M:%S")
		Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		session = Session()
		user_id = session.query(User._id).count()+1
		userX= User(_id=user_id, date=current_time, name=name, mail=mail, commentaire=comme)
		session.add(userX)
		session.commit()
		return userX
		
	def recup_stats(self, text_input, text_output, nb_mot_E, frq_mot_E, nb_carac_E, nb_mot_S, frq_mot_S, nb_carac_S, diff_mot, diff_carac):
		
		Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		session = Session()
	
		stats_id = session.query(Stats.id_stat).count()+1
		now = datetime.now()
		current_time = now.strftime("%Y/%m/%d %H:%M:%S")
		
		statX = Stats(id_stat = stats_id, date=current_time, text_input=text_input, text_output=text_output, nb_mot_E=nb_mot_E, frq_mot_E=frq_mot_E, nb_carac_E=nb_carac_E, nb_mot_S=nb_mot_S, frq_mot_S=frq_mot_S, nb_carac_S=nb_carac_S, diff_mot = diff_mot, diff_carac = diff_carac) 
		
		session.add(statX)
		session.commit()
		
		return statX
		
		
class dbs_utils():
 	
	def nb_mot(self, text):
		nb_mot = len(text.split())
		return nb_mot
		
	
	def frq_mot(self, text):
		liste_mot = text.split()
		str2 = []
		dic_frq={}
		for i in liste_mot:             
			if i not in str2:
				str2.append(i) 
		for i in range(0, len(str2)):
			dic_frq[str2[i]] = liste_mot.count(str2[i])
		return list(dic_frq.keys()), list(dic_frq.values())

	
	
	def nb_carac(self, text):
		nb_carac = len(text)
		return nb_carac
		
		
	def dif_mot(self, texte_E, texte_S):
		dif_mot = self.nb_mot(texte_E) - self.nb_mot(texte_S)
		taux_reduc_mot = (1 - (self.nb_mot(texte_S) / self.nb_mot(texte_E))) * 100
		return dif_mot, taux_reduc_mot
		
		
	def dif_carac(self, texte_E, texte_S):
		dif_carac = self.nb_carac(texte_E) - self.nb_carac(texte_S)
		taux_reduc_carac = (1 - (self.nb_carac(texte_S) / self.nb_carac(texte_E))) * 100
		return dif_carac, taux_reduc_carac		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
