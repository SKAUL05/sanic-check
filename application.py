from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger
from requests import get
import json as js

app = Sanic()
search_data = {}

def filter_country_data(cy_data):
    for country in cy_data:
        search_data[country['alpha3Code']] = country
    logger.info(len(search_data))
    return search_data


def country_stats(search_data,ccode):
    info = {}
    if ccode in search_data:
        return search_data[ccode]
    else:
        return {}


@app.route("/countries")
async def countries(request):
    logger.info("Countries")
    cy_data = js.loads(get("https://restcountries.eu/rest/v2/all").text)
    logger.info(len(cy_data))
    search_data = filter_country_data(cy_data)
    return json(search_data)
    
@app.route("/country-info")
async def info(request):
    in_data = country_stats(search_data,"AFG")
    return json(in_data)

@app.route("/")
async def test(request):
    logger.info("Initialized")
    ip = get('https://api.ipify.org').text
    return json({"IP": ip})

