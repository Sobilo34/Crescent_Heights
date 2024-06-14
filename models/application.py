from sqlalchemy import Column, String, Text, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Application(BaseModel, Base):
    """Representation of a student application data and methods"""
    __tablename__ = 'applications'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    phone = Column(String(15), nullable=False)
    address = Column(Text, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    grade_applying_for = Column(String(10), nullable=False)
    previous_school = Column(String(128), nullable=True)
    parent_name = Column(String(128), nullable=False)
    parent_contact = Column(String(15), nullable=False)
    status = Column(String(20), default='Pending')  # Status of the application
    documents = relationship('Document', back_populates='application')

    def __init__(self, *args, **kwargs):
        """initializes application"""
        super().__init__(*args, **kwargs)

    def set_status(self, status):
        """Sets the status of the application"""
        self.status = status

    def add_document(self, document):
        """Adds a document to the application if under 5 documents"""
        if self.documents.count() < 5:
            self.documents.append(document)
        else:
            raise Exception("Cannot add more than 5 documents to an application")
