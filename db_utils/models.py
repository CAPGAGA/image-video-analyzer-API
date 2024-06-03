from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from .db import Base


class UploadedFile(Base):

    __tablename__ = 'uploaded_files'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    result_id = Column(Integer, ForeignKey('analysis_results.id'), default=None)
    file_name = Column(String, unique=True)
    uploaded = Column(DateTime(), server_default=func.now())
    result = relationship("Result", back_populates='uploaded_files')

class Results(Base):

    __tablename__ = 'analysis_results'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    file_id = Column(Integer, ForeignKey('uploaded_files.id'))
    result = Column(String)
    created = Column(DateTime(), onupdate=func.now())

    from_file = relationship("UploadedFile", back_populates='from_file')