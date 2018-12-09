from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base(

)


class Status(Base):
    __tablename__ = 'eth_addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address = Column(String)
    balance = Column(BigInteger)
    transactions = Column(BigInteger)
    asof = Column(DateTime)

    def __repr__(self):
        return {'id': self.id, 'name': self.address, 'balance': self.balance, 'transactions': self.transactions,
                'asof': self.asof.isoformat(' ')}


def init(path):
    engine = create_engine(path, echo=True)
    Base.metadata.create_all(engine)
    return engine


def session(path='sqlite:///:memory:'):
    Session = sessionmaker(bind=init(path))
    return Session( )
