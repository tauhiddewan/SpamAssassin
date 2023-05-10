import os
import yaml
from pathlib import Path
from dotenv import dotenv_values
secrets = dotenv_values(".env")
os.environ['KAGGLE_USERNAME'] = secrets["username"]
os.environ['KAGGLE_KEY'] = secrets["key"]
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


ROOT = Path(__file__).parent
config_path = ROOT/ "confs.yaml"
config = yaml.safe_load(open(config_path))

# api.dataset_download_files("https://www.kaggle.com/competitions/nlp-getting-started/data", path=config["data"]["dataset"])
api.dataset_download_files('Cornell-University/arxiv',
                           path=config["data"]["dataset"])