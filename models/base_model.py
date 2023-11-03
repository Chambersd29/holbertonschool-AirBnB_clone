#!/usr/bin/python3
"""
Este módulo define la clase BaseModel
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Esta es la clase que heredarán las demas clases
    """

    def __init__(self, *args, **kwargs):
        """
        Este método inicializa los atributos:
            id, created_at, updated_at
        Args:
            **kwargs: recibe un diccionario.
        """
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)

            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.__dict__["updated_at"] = datetime.strptime(
                self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Este metodo retorna una representación de nuestra instancia
        """

        # return "[{}] ({}) {}".format(self.__class__.__name__,
        #                              self.id, self.__dict__)

        return f"[{type(self).__name__}] ({self.id}) " \
            + str({k: v for k, v in self.__dict__.items() if k != '__class__'})

    def save(self):
        """
        Este método actualiza la fecha de creación updated_at.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Este método retorna un diccionario con los atributos de instancia.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
