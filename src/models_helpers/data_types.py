from abc import ABC, abstractmethod

from ..logger.logger import LoggerFactory
log = LoggerFactory.get_logger("unknown_data_type")


class DataType(ABC):
    ALLOWED_VALUES = set()

    def __init__(self, value, when_unknown="Unknown"):
        if value not in self.ALLOWED_VALUES:
            log.info(
                f"Se intentó insertar '{value}' como {self.__class__.__name__}. "
                f"Debe ser uno de {self.ALLOWED_VALUES}. Se le asigna '{when_unknown}' al no ser reconocido."
            )
            self.value = when_unknown
        else:
            self.value = value

    def __str__(self):
        return self.value


class ClassDataType(DataType):
    ALLOWED_VALUES = {"Low", "Medium", "High"}


class ResistantDataType(DataType):
    ALLOWED_VALUES = {"Durable", "Weak"}
