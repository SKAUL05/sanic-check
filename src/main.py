from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger

app = Sanic("hello_example")

@app.route("/test")
async def test(request):
    logger.info("Initialized")
    return json({"hello": "world"})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)