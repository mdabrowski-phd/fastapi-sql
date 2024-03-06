from sqlalchemy import Column, Integer, Boolean, VARCHAR, create_engine, between, and_, desc, func
from sqlalchemy.sql.expression import false
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Table, MetaData


user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "postgres"


Base = declarative_base()

connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()


class TaskTable(Base):
    __tablename__ = "tasks"

    id_number = Column("id", Integer, primary_key=True)  # auto-increment included
    description = Column("description", VARCHAR(30), nullable=False)
    priority = Column("priority", Integer)
    is_complete = Column("is_complete", Boolean, nullable=False, server_default=false())

    def __repr__(self):
        return f"Task(id={self.id_number})"


class UserTable(Base):
    __tablename__ = "users"

    id_number = Column("id", Integer, primary_key=True)
    username = Column("username", VARCHAR(20), nullable=False)
    password = Column("password", VARCHAR(30), nullable=False)
    is_admin = Column("is_admin", Boolean, nullable=False, server_default=false())

    def __repr__(self):
        return f"User(id={self.id_number})"


# Base.metadata.create_all(bind=engine)

# *** INSERT ***

# description = "Task description"
# priority = 2
# is_complete = True

# task = TaskTable(description=description, priority=priority, is_complete=is_complete)

# session.add(task)
# session.commit()

# description = "Task2 description"
# priority = 1
# is_complete = False

# task = TaskTable(description=description, priority=priority)
#
# session.add(task)
# session.commit()

# description = "Task3 description"
# priority = 2
# is_complete = False

# task = TaskTable(description=description, priority=priority)
#
# session.add(task)
# session.commit()

# *** SELECT ***

# All Data
results = session.query(TaskTable).all()
print(results)
print(results[0].priority)

# One Row
results = session.query(TaskTable).first()
print(results)

# Columns
results = session.query(TaskTable.description, TaskTable.is_complete).all()
print(results)

# *** Filter (WHERE) ***
results = session.query(TaskTable).filter_by(is_complete=False).all()
print(results)

results = session.query(TaskTable).filter_by(id_number=2).all()
print(results)

results = session.query(TaskTable).filter(and_(between(TaskTable.priority, 1, 2),
                                               between(TaskTable.id_number, 1, 2))).all()
print(results)

# *** SORT ***

results = session.query(TaskTable).order_by(desc(TaskTable.priority)).all()
print(results)

results = session.query(TaskTable).order_by(desc(func.length(TaskTable.description))).all()
print(results)

# *** GROUP BY ***

results = session.query(TaskTable.is_complete, func.count(TaskTable.id_number)).group_by(TaskTable.is_complete).all()
print(results)

results = session.query(TaskTable.is_complete, func.avg(TaskTable.priority)).group_by(TaskTable.is_complete).all()
print(results)

# *** UPDATE ***

# one() instead of first() if only one result expected
record_to_update = session.query(TaskTable).filter(TaskTable.id_number == 2).one()
record_to_update.is_complete = True

# session.commit()

# *** DELETE ***

record_to_delete = session.query(TaskTable).filter(TaskTable.id_number == 2).one()
session.delete(record_to_delete)

# session.commit()

# *** TABLE DROP ***

metadata = MetaData()
table_to_drop = Table('tasks', metadata, autoload_with=engine)

# table_to_drop.drop(engine)
