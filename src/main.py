from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger
from requests import get
import json as js

app = Sanic("hello_example")

def filter_country_data(cy_data):
    search_data = dict()
    for country in cy_data:
        search_data[country['alpha3Code']] = country
    logger.info(len(search_data))
    return search_data



@app.route("/countries")
async def countries(request):
    logger.info("Countries")
    cy_data = js.loads(get("https://restcountries.eu/rest/v2/all").text)
    logger.info(len(cy_data))
    search_data = filter_country_data(cy_data)
    return json(search_data)
    

@app.route("/")
async def test(request):
    logger.info("Initialized")
    ip = get('https://api.ipify.org').text
    return json({"IP": ip})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)