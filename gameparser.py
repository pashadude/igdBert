from pathlib import Path
from igdb_api_python.igdb import igdb
import settings

class GamesRewiewParser():

    def __init__(self, data_path='gamedata/', class_path='gamedata/igdb_class/'):
        self.classes = []
        self.data_path = Path(data_path)
        self.class_path = Path(class_path)
        self.igdb = igdb(settings.igdb_key)

    def create_path_folders(self):
        self.data_path.mkdir(exist_ok=True)
        self.class_path.mkdir(exist_ok=True)

class GameReviewAnalyser():

    def __init__(self, ):
        self.data = []