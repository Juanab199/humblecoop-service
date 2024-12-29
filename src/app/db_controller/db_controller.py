from sqlalchemy.orm import Session
from alchemical import Alchemical

from app.config.env import DATABASE_URL
from app.exceptions.exceptions import NotRegistryFound

db = Alchemical(DATABASE_URL)

class DatabaseConnection:
    def __init__(self, session: Session = None):
        self.db_session = session
    
    def push_db_registry(self, item_to_save):
        self.db_session.add(item_to_save)
        self.db_session.commit()
        self.db_session.refresh(item_to_save)
        
    def get_db_registry_by_id(self, id: int, table):
        found_registry = self.db_session.query(table).filter(table.id == id).first()
        if found_registry is None:
            raise NotRegistryFound
        return found_registry
    
    def get_db_registries_by_column(self, column, values, table):
        column_attr = getattr(table, column, None)
        if column_attr is None:
            raise AttributeError(f"La tabla {table.__name__} no tiene una columna llamada {column}")
        
        found_registries = self.db_session.query(table).filter(column_attr.in_(values)).all()
        
        if found_registries is None:
            raise NotRegistryFound
        return found_registries

    def get_db_all_registries_from_table(self, table):
        registries = self.db_session.query(table).all()
        return registries
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.db_session.rollback()
        self.db_session.close()
        
        
def get_db_connection():
    with DatabaseConnection(session=db.Session()) as db_connection:
        yield db_connection