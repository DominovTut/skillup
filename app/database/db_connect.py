from sqlalchemy import create_engine


from app.database.models import Base


sqlite_connection_string = "sqlite:///db.sqlite3"
db_engine = create_engine(sqlite_connection_string)

Base.metadata.create_all(db_engine)
