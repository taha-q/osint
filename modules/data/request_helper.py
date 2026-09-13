import random

captcha_related_words: list[str] = [
        # cloudflare_triggers
        "Attention Required! | Cloudflare",
        "Checking your browser before accessing",
        "DDoS protection by Cloudflare",
        "cf-chl-widget",
        "cf-chl-bypass",
        "challenges.cloudflare.com"
        # captcha_triggers
        "Please verify you are a human",
        "Access denied",
        "Robot verification",
        "Complete the security check to continue",
        "g-recaptcha",
        "h-captcha",
        "g-recaptcha-response"
        # akamai_perimeterx_triggers
        "Access Denied - You don't have permission to access",
        "Reference #",
        "Please enable JavaScript to view this page",
        "perimeterx"
        # rate_limit_triggers 
        "Too many requests",
        "You have been blocked",
        "Your IP has been temporarily rate limited"
    ] 
headers: list[dict] = [
    # Type 1: Desktop Chrome Profile
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    },
    # Type 2: Desktop Firefox Profile
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    },
    # Type 3: Mobile Safari (iOS) Profile
    {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    ]

class RequestHelper:

    @staticmethod
    def _get_human_headers() -> dict:
        """
        returns randomized headers for each call
        """
        return random.choice(headers)


    @staticmethod
    def validate_success_via_html(text) -> bool:
        """
        parsers a set html and rated based on a score (1/10)
        :param text: the html to parse
        """

        score:int = 10

        if text.lower() in captcha_related_words:
            score = 0

        return score >= 5
        