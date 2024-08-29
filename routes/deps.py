from db.connection import session

def get_conection():
    try:
        db_session = session()
        yield db_session
    except:
        db_session.close()
