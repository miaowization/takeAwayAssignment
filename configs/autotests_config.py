# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.environ.get('BASE_URL', 'localhost')
