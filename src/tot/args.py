import argparse
import json
from tot.tasks.base import CACHE_PATH

TEMP_CONFIG = 'temp_config.json'

def save_args(args: argparse.Namespace):
    json.dump(args.__dict__, open(TEMP_CONFIG, 'w'))