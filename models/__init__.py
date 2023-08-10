#!/usr/bin/python3
"""
Initialization script for the models directory.
Creates an instance of FileStorage and reloads data from file.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
