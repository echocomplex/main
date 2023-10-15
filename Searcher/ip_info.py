"""

SEARCH_IP_INFO Function for Searcher bot
(https://t.me/searcher_info_bot (@searcher_info_bot))
Creator - echo complex (https://t.me/echoscomplex)
Licence - GNU GPL v2 ECHO'S DEVELOPMENT © 2023 (https://t.me/echoscode)


<< DESCRIPTION FOR DEVELOPERS >>

You can see an example in «if (__name__=="__main__")»

"""


# imports
import requests


# class functions
class Ip_Get_Info:
    # local variables
    def __init__(self, ip_address: str):
        self.__url: str = f"http://ip-api.com/json/{ip_address}";  # create url
        self.__info = requests.get(url=self.__url).json();  # try request
        self.city: str = self.__info.get('city');
        self.regionName: str = self.__info.get('regionName');
        self.country: str = self.__info.get('country');
        self.isp: str = self.__info.get('isp');
        self.org: str = self.__info.get('org');
        self.zip: str = self.__info.get('zip');
        self.timezone: str = self.__info.get('timezone');
        self.lat: str = self.__info.get('lat');
        self.lon: str = self.__info.get('lon');



if (__name__ == "__main__"):
    ip_address: str = "<<Any IP Address>>";
    info = Ip_Get_Info(ip_address);
    print(info.country, info.city, info.regionName, info.isp,
          info.org, info.zip, info.timezone, info.lat, info.lon);
