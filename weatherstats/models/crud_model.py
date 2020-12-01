from abc import ABC, abstractmethod


class CrudModel(ABC):
    """
    Base class for models with CRUD capabilities (create, read, update,
    delete), talking to a database.

    :author: Johan Nilsson
    :since:  0.1.0
    """

    @abstractmethod
    def create(self):
        pass
