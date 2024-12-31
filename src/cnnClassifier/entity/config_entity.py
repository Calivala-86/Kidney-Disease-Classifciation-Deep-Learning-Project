from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfg:
    root_dir: Path
    source_URl: str
    local_data_file: Path
    unzip_dir: Path
