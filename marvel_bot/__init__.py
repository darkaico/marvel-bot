import os

import sentry_sdk
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SENTRY_SDK_KEY = os.getenv("SENTRY_SDK_KEY")

sentry_sdk.init(SENTRY_SDK_KEY, traces_sample_rate=1.0)
