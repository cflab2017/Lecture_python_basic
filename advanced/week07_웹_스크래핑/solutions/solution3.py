from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

def can_crawl(url: str, user_agent: str = "*") -> bool:
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception:
        return True   # robots.txt 못 읽으면 일단 허용으로 처리
    return rp.can_fetch(user_agent, url)

print(can_crawl("https://www.python.org/about/"))
print(can_crawl("https://www.google.com/search?q=python"))
