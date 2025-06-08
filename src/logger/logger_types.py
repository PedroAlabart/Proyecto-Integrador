import json
from datetime import datetime


class DataTypeLogger:
    def __init__(self, logger):
        self.logger = logger

    def log_invalid_value(self, class_name, value, allowed_values, assigned_value):
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "level": "INFO",
            "event": "unknown_data_type",
            "data_type": class_name,
            "invalid_value": value,
            "allowed_values": list(allowed_values),
            "assigned_value": assigned_value,
        }
        self.logger.info(json.dumps(log_data, ensure_ascii=False))
