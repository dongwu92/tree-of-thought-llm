import argparse
import json
import os

from tot.args import TEMP_CONFIG
from tot.tasks.base import CACHE_PATH


class PromptCache:
    def __init__(self) -> None:
        self.args = json.load(open(TEMP_CONFIG))
        self.path = CACHE_PATH + '/cache'
        for k in self.args.keys():
            self.path += '_' + k + '-' + str(self.args[k])
        self.path += '.json'
        self.data = {}
        if os.path.exists(self.path):
            self.data = json.load(open(self.path))
    
    def save(self):
        json.dump(self.data, open(self.path, 'w'), indent=4)
    
    def find(self, prompt):
        if prompt in self.data:
            return self.data[prompt]
        return None
    
    def cache(self, prompt, responses, save=False):
        self.data[prompt] = responses
        if save:
            self.save()

pcache = PromptCache()