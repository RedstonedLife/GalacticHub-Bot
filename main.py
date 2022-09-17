import discord
import json
import logging
import os
import datetime
import sqlite3
import asyncio
from discord.ext import commands
from discord.utils import get, find
import random

from utilities.Constants import *


def initLogger() -> logging.Logger:
    lg = logging.getLogger("GLHUB_LOG")
    lg.setLevel(logging.DEBUG)
    handler = logging.FileHandler(
        filename=f"logs/bot-{datetime.datetime.now().strftime('%d-%m-%Y')}.log",
        encoding="utf-8",
        mode="a"
    )
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s:%(levelname)s:%(name)s: %(message)s"
        )
    )
    lg.addHandler(handler)
    return lg


def initConfig() -> json:
    try:
        with open("cfgs/bot.json", "r") as f:
            data = json.loads(f.read())
            f.close()
            return data
    except Exception as e:
        print(e)
        exit(-1)


def initdbConfig() -> json:
    try:
        with open("cfgs/database.json", "r") as f:
            data = json.loads(f.read())
            f.close()
            return data
    except Exception as e:
        print(e)
        exit(-1)
