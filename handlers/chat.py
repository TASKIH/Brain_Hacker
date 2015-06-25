# -*- coding: utf-8 -*-
import random
from collections import defaultdict

class Chat(object):

    cache_size = 200
    user_num = list(range(1, 100))
    random.shuffle(user_num)

    def __init__(self):
        self.cache = defaultdict(list)

    def update_cache(self, chat, room_id):
        self.cache[room_id].append(chat)
        if len(self.cache[room_id]) > self.cache_size:
            self.cache[room_id] = self.cache[-self.cache_size:]

    def get_random_name(self):
        return self.user_num.pop()