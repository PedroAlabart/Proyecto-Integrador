import logging
import os


class LoggerFactory:
    """
    LoggerFactory no se instancia, se usa solo su static method get_logger
    """
    _loggers = {}

    @staticmethod
    def get_logger(name: str,
                   log_dir: str = "logs",
                   filename: str = "",
                   level: int = logging.DEBUG,
                   encoding: str = "utf-8",
                   formatter: logging.Formatter = None) -> logging.Logger: # type: ignore
        """
        Devuelve un logger configurado con un archivo de salida y opcionalmente consola.
        Utiliza cache para evitar múltiples instancias del mismo logger.
        """
        if name in LoggerFactory._loggers:
            return LoggerFactory._loggers[name]

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        if not filename:
            filename = f"{name}.log"

        filepath = os.path.join(log_dir, filename)
        file_handler = logging.FileHandler(filepath, encoding=encoding)

        if formatter is None:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(file_handler)
        logger.propagate = False  # evita que se duplique la salida

        LoggerFactory._loggers[name] = logger
        return logger
