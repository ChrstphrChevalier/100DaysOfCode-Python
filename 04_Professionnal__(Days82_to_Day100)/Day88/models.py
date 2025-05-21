from sqlalchemy import Column, Integer, String, Boolean
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Coffee(db.Model):
    __tablename__ = 'coffee'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    adress = Column(String, nullable=False)
    website = Column(String)
    wifi = Column(Boolean, nullable=False)
    prises = Column(Boolean, nullable=False)
    image_url = Column(String)

    def __repr__(self):
        return f"<Cafe(name='{self.name}', adress='{self.adress}', wifi={self.wifi}, prises={self.prises})>"
