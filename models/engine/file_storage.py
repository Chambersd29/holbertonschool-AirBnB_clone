#!/usr/bin/python3
import json
from os import path


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):

        new_dict = {}

        for k, obj in FileStorage.__objects.items():
            new_dict[k] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        if not path.exists(FileStorage.__file_path):
            return
        else:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objs = json.load(f)

            for k, v in objs.items():
                from models.base_model import BaseModel

                bs = BaseModel(**v)
                FileStorage.__objects[k] = bs
