from typing import Dict, List

from linker import EntityLinker
from recognizer import EntityRecognizer


class EntityResolver:
    def __init__(self, recognizer: EntityRecognizer, linker: EntityLinker):
        self.recognizer = recognizer
        self.linker = linker

    def process(self, chara_table: Dict[str, List[str]], doc: str):
        pass
