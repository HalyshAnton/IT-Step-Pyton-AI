from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Sequence
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']  # postgres
    db_password = data['password']

db_url = f'postgresql+pg8000://{db_user}:{db_password}@localhost:5432/People'
engine = create_engine(db_url)

# Оголошення базового класу
Base = declarative_base()


# Визначення класу моделі для користувачів
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(50))

    projects = relationship('Projects', back_populates='users',
                            secondary='user_projects')


# Визначення класу моделі для проектів
class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, Sequence('project_id_seq'), primary_key=True)
    name = Column(String(100), unique=True)

    users = relationship("Users", back_populates='projects', # колонка з таблиці users
                         secondary='user_projects'  # таблиця user_projects
                         )


# Визначення асоціаційної таблиці
class UserProject(Base):
    __tablename__ = 'user_projects'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'), primary_key=True)


Base.metadata.create_all(bind=engine)

