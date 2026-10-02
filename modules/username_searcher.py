import aiohttp
import asyncio
from .data.osint_data_class import OsintDataClass
from .data.request_helper import RequestHelper

class UsernameSearcher:
    def __init__(self):
        self.websites:dict[str,str] = OsintDataClass.username_search_websites
        self.session = None

 

    async def search(self, username:str, timeout:float) -> None:
        """
        searches a username across a list of websites

        :param username: the target username
        :param timeout:  time before closing the connection
        :rtype: None
        """
        print(f"+ loaded {len(self.websites)} websites")

        try:
            for site_info in self.websites:
                name = site_info["name"]
                url  = site_info["url"].format(username)

                response = await self.session.get(url, timeout=timeout, headers=RequestHelper._get_human_headers())
                response.raise_for_status()

                if RequestHelper.validate_success_via_html(await response.text()):
                    print(f"% found on : {name:<5} | +link: {url}")
        except (asyncio.TimeoutError, aiohttp.ClientError) as e:
            ...


    async def __aenter__(self):
        if not self.session:
            self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        
        return self


    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.session:
            await self.session.close()
