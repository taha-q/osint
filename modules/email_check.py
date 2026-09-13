import aiodns

class EmailChecker:
    def __init__(self):
        self.resolver:aiodns.DNSResolver|None =  None

    async def is_valid_email(self, email:str) -> bool:
        """checks if the given email is valid

        :rtype: bool    
        :param email: the email 
        """
        # syntax check
        parts: list[str] = email.split("@")
        if len(parts) < 2: return False

        # query MX records
        try:
            records = await self.resolver.query_dns(parts[1], "MX")
            if records:
                return True

        except aiodns.error.DNSError:
            return False

    
    async def check_breach_sites(self, email:str) -> list[str] | None:
      """Check for data breaches across known websites.

         :param email: The target email address to check.
         :return: A list of websites where data breaches were identified.
         :rtype: list
       """

    async def __aenter__(self):
        if not self.resolver:
            self.resolver = aiodns.DNSResolver()

        return self
    
    async def __aexit__(self, exc_value, exc_type, traceback):
        if self.resolver:
            # turns out aiodns uses pycares, to manages its life-cycle automaticly
            pass