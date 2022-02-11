import json
from pathlib import Path
import requests


def serialize_json_file(data: dict, path_obj: Path, mode: str = "w"):
    with path_obj.open(mode) as write_obj:
        json.dump(data, write_obj, indent=4)


def deserialize_json_file(path_obj: Path, mode: str = "r"):
    with path_obj.open(mode) as read_file:
        return json.load(read_file)


def download_file(url: str,
                  local_write: Path,
                  mode: str = 'wb',
                  chunk_size: int = 1024):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with local_write.open(mode) as fo:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fo.write(chunk)
    return local_write
