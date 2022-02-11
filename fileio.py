import json
from pathlib import Path

def cache_data_to_json(data: dict,
                       path_obj: Path,
                       mode: str = 'w'):
    with path_obj.open(mode) as write_obj:
        json.dump(data, write_obj, indent=4)


def deserialize_from_json(path_obj: Path,
                          mode: str = 'r'):
    with path_obj.open(mode) as read_file:
        return json.load(read_file)

