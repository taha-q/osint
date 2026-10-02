class OsintDataClass:
    username_search_websites:list[dict] = [
    {"name": "github", "url": "https://github.com/{}"},
    {"name": "twitter", "url": "https://x.com/{}"},
    {"name": "instagram", "url": "https://instagram.com/{}"},
    {"name": "reddit", "url": "https://reddit.com/user/{}"},
    {"name": "youtube", "url": "https://youtube.com/@{}"},
    {"name": "linkedin", "url": "https://linkedin.com/in/{}"},
    {"name": "tiktok", "url": "https://tiktok.com/@{}"},
    {"name": "facebook", "url": "https://facebook.com/{}"},
    {"name": "pinterest", "url": "https://pinterest.com/{}"},
    {"name": "twitch", "url": "https://twitch.tv/{}"},
    {"name": "steam", "url": "https://steamcommunity.com/id/{}"},
    {"name": "soundcloud", "url": "https://soundcloud.com/{}"},
    {"name": "medium", "url": "https://medium.com/@{}"},
    {"name": "behance", "url": "https://behance.net/{}"},
    {"name": "dribbble", "url": "https://dribbble.com/{}"},
    {"name": "gitlab", "url": "https://gitlab.com/{}"},
    {"name": "stackoverflow", "url": "https://stackoverflow.com/users/{}"},
    {"name": "spotify", "url": "https://open.spotify.com/user/{}"},
    {"name": "telegram", "url": "https://t.me/{}"},
    {"name": "hackernews", "url": "https://news.ycombinator.com/user?id={}"}
]
