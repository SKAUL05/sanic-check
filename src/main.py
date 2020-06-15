from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger
from requests import get
import json as js



app = Sanic("hello_example")

@app.route("/countries")
async def countries(request):
    logger.info("Countries")
    cy_data = js.loads(get("https://restcountries.eu/rest/v2/all").text)
    logger.info(cy_data)
    return json(cy_data)
    

@app.route("/")
async def test(request):
    logger.info("Initialized")
    ip = get('https://api.ipify.org').text
    return json({"IP": ip})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)