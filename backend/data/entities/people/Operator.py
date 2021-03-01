#  AmazRT  -  Parcel Management System
#  First semester Technical Degree project
#
#  Copyright  (c) 2021 - 2022
#  - Meryem KAYA @MeryemKy
#  - Alexis LEBEL @Alestrio
#  - Malo LEGRAND @HoesMaaad
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

from backend import Base


class Operator(Base):
    """
    @Entity
    This is the entity class responsible for operator data management.
    The tablename is "personnel"
    """
    __tablename__ = 'personnel'
    id_operator = Column('id_personnel', Integer, primary_key=True)
    id_pld = relationship('pld', foreign_keys='pld.is_pld')
    lastname = Column('nom_personnel', VARCHAR(50))
    firstname = Column('prenom_personnel', VARCHAR(50))
    login = Column('login_personnel', VARCHAR(15))
    password = Column('mdp_personnel', VARCHAR(15))

    def __init__(self,
                 id_operator, id_pld, lastname, firstname, login, password):
        super().__init__()
        self.id_operator = id_operator
        self.id_pld = id_pld
        self.lastname = lastname
        self.firstname = firstname
        self.login = login
        self.password = password
