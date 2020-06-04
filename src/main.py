from sanic import Sanic
from sanic.response import json, text, html
from sanic.log import logger

from jinja2 import Environment, PackageLoader, select_autoescape


app = Sanic("hello_example")
env = Environment(loader=PackageLoader("main", "templates"))

env = Environment(
    loader=PackageLoader("main", "templates"),
    autoescape=select_autoescape(["html", "xml", "tpl"]),
)


def template(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))


@app.route("/test")
async def test(request):
    logger.info("Initialized")
    return json({"hello": "world"})


@app.route("/")
async def default(request):
    logger.info("Template Render")

    return template("index.html", title="Sanic")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
