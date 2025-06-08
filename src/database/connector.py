from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_engine()
        return cls._instance

    def _initialize_engine(self):
        user = config("DB_USER")
        password = config("DB_PASSWORD")
        host = config("DB_HOST")
        port = config("DB_PORT")
        db = config("DB_NAME")

        connection_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        self.engine: Engine = create_engine(connection_url,
                                            pool_pre_ping=True, # Create Engine tiene lazy instiation. El atributo pool_pre_ping hace un ping para ver que la db funciona
                                            echo=True #Activa un log mas completo
                                            )
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()


