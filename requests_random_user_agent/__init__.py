import os
import random

import requests.utils


USER_AGENTS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'useragents.txt')
USER_AGENTS = open(USER_AGENTS_FILE).readlines()

requests.utils.default_user_agent = lambda: random.choice(USER_AGENTS)