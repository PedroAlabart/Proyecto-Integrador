from abc import ABC
from ..logger.logger_factory import LoggerFactory
from ..logger.logger_types import DataTypeLogger

log = LoggerFactory.get_logger("unknown_data_type")
data_type_logger = DataTypeLogger(log)

class DataType(ABC):
    ALLOWED_VALUES = set()

    def __init__(self, value, when_unknown="Unknown"):
        if value not in self.ALLOWED_VALUES:
            data_type_logger.log_invalid_value(
                self.__class__.__name__,
                value,
                self.ALLOWED_VALUES,
                when_unknown
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
