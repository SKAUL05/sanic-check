from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger
from requests import get



app = Sanic("hello_example")

@app.route("/")
async def test(request):
    logger.info("Initialized")
    ip = get('https://api.ipify.org').text
    return json({"IP": ip})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)