import database as _database

def create_database():
  return _database.Base.metadata.create_all(bind=_database.engine)
  # 실제 데이터베이스 생성 코드