import datetime as _dt
from pydantic import BaseModel
# 간단하게 입력할 데이터의 힌트를 주는 것이라고 생각

class _UserBase(BaseModel):
  email: str
  # email은 문자열로 입력하라고 힌트주는 것


class UserCreate(_UserBase):
  hashed_password: str

  class Config:
    orm_mode = True


class User(_UserBase):
  id: int

  class Config:
    orm_mode = True


class _LeadBase(BaseModel):
  first_name: str
  last_name: str
  email: str
  company: str
  note: str


class LeadCreate(_LeadBase):
  pass


class Lead(_LeadBase):
  id: int
  owner_id: int
  date_created: _dt.datetime
  date_last_updated: _dt.datetime

  class Config:
    orm_mode = True