# TODO: read in your yaml file and parse it using the data classes defined in dataclasses.py
import yaml
from pathlib import Path
from config_schema import Config


def load_config(config_path: str = "../config.yaml") -> Config:
    with open(config_path, "r") as file:
        config_dict = yaml.safe_load(file)
    return Config(**config_dict)

if __name__ == "__main__":
    config = load_config()
    print(config.data.data_path)        
    print(config.model.params.max_iter) 
