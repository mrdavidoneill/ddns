import os
import urllib.request as request
import xml.etree.ElementTree as xmltree
from logger import logger
from dotenv import load_dotenv

# Get environment variables
load_dotenv()
host = os.environ.get("HOST")
domain_name = os.environ.get("DOMAIN")
ddns_password = os.environ.get("PASSWORD")

# XML root keys
IP = 2
ERROR_COUNT = 3
DONE = 5

URL = f"https://dynamicdns.park-your-domain.com/update?host={host}&domain={domain_name}&password={ddns_password}"

with request.urlopen(URL) as response:
    xml = response.read()
    root = xmltree.fromstring(xml)

    ip = root[IP].text
    error_count = root[ERROR_COUNT].text
    done = root[DONE].text

    logger.info(f"@{ip}, {error_count} errors and done: {done}")
