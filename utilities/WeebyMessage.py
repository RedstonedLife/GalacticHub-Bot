import json
import discord
import random

with open("cfgs/weeb_emotes.json") as f:
    data = json.load(f)


class WeebyMessages:
    def __init__(self, d, type: str = None, member: discord.Member = None, to: discord.Member = None,
                 is_self: bool = False):
        self.member = member
        self.to = to
        self.type = type
        self.is_self = is_self
        self.d = d
        self.get_random()
        self.replace()

    def get_random(self):
        if self.is_self == True and self.d == "uEmote":
            self.message = str(random.choice(data[self.d][str(self.type)]['self']))
            return
        if self.is_self:
            self.message = str(random.choice(data[self.d][str(self.type)]['msg']))
        else:
            self.message = random.choice(data[self.d][str(self.type)]['msg'])

    def replace(self):
        if self.is_self:
            self.message = self.message.replace("?", self.member.display_name, 1)
        else:
            self.message = self.message.replace("?", self.member.display_name, 1).replace("?", self.to.display_name)

    def __message__(self):
        return self.message
