from sanic import Sanic
from sanic.response import json, text, html
from sanic.log import logger

from jinja2 import Environment, PackageLoader


app = Sanic("hello_example")
env = Environment(loader=PackageLoader("main",'templates'))


@app.route("/test")
async def test(request):
    logger.info("Initialized")
    return json({"hello": "world"})

@app.route("/")
async def default(request):
    logger.info("Template Render")
    template = env.get_template('index.html')
    html_content = template.render()
    return html(html_content)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug = True, port=8000)