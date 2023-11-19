# Визначення моделей даних для бази даних

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
import datetime

Base = declarative_base()


def current_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Roles(Base):
    __tablename__ = 'roles'

    role = Column(String, primary_key=True, nullable=False)
    description = Column(String)


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String)
    email = Column(String, nullable=False)
    role = Column(String, ForeignKey('roles.role'), nullable=False)
    created_at = Column(String, nullable=False, 
                        default=current_timestamp())


class BugStatuses(Base):
    __tablename__ = 'bug_statuses'

    status = Column(String, primary_key=True, nullable=False)
    description = Column(String)


class Priorities(Base):
    __tablename__ = 'priorities'

    priority = Column(String, primary_key=True, nullable=False)


class Bugs(Base):
    __tablename__ = 'bugs'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String, ForeignKey('bug_statuses.status'), default='NEW')
    priority = Column(String, ForeignKey('priorities.priority'))
    created_at = Column(String, nullable=False, default=current_timestamp())
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)
    assigned_to = Column(Integer, ForeignKey('users.id'), nullable=False)
    is_open = Column(Integer, nullable=False, default=1)


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, nullable=False)
    bug_id = Column(Integer, ForeignKey('bugs.id'), nullable=False)
    comment = Column(String, nullable=False)
    created_at = Column(String, nullable=False, default=current_timestamp())
    created_by = Column(Integer, ForeignKey('users.id'), nullable=False)