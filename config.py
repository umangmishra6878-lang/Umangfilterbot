# =========================================================
#                CINEMA HUB – BOT CONFIG
# =========================================================

# -------- TELEGRAM CORE --------
API_ID = 123456
API_HASH = "API_HASH_HERE"
BOT_TOKEN = "BOT_TOKEN_HERE"

BOT_NAME = "Cinema Hub Autofilter"
BOT_USERNAME = "CinemaHubBot"

# -------- DATABASE --------
MONGO_URI = "MONGO_URI_HERE"
DATABASE_NAME = "cinema_hub"

# -------- ADMINS --------
ADMINS = [
    123456789,   # Owner
]

# -------- CHANNELS / GROUPS --------
UPDATE_CHANNEL = -1001111111111      # Movie + TV updates
LOG_CHANNEL = -1002222222222         # Errors, logs
BIN_CHANNEL = -1003333333333         # Silent cache
REQUEST_GROUP = -1004444444444       # Request group
SUPPORT_GROUP = -1005555555555       # Support / help

# -------- FORCE SUB --------
FORCE_SUB_CHANNEL = -1006666666666
FORCE_SUB = True

# -------- VERIFY SYSTEM --------
VERIFY_CHANNEL = -1007777777777
VERIFY_TIMEOUT = 300   # seconds

# -------- PREMIUM SYSTEM --------
PREMIUM_ENABLED = True
PREMIUM_LOG_CHANNEL = -1008888888888

# -------- SHORTNER SYSTEM --------
SHORTNER_ENABLED = True
SHORTNER_API = "SHORTNER_API_KEY"
SHORTNER_DOMAIN = "example.com"

# -------- AUTO FILTER SETTINGS --------
MAX_RESULTS = 10
ENABLE_TV_SERIES = True
ENABLE_MOVIES = True
ENABLE_UPDATE_POST = True

# -------- FLOOD / SECURITY --------
ANTI_SPAM = True
SPAM_LIMIT = 5
SPAM_TIME = 10  # seconds

# -------- FUTURE STREAMING (READY) --------
STREAMING_ENABLED = False
STREAM_BASE_URL = "https://cinema-hub-streaming.onrender.com"

# =========================================================