import sys
import os

# Add the parent directory of "tiktok_manager" to sys.path
# So we can use the parent folder without making them on packages!
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# If script doesn't work, especially upload_bot, add it manually in you system path variables!