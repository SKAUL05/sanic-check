from sanic import Sanic
from sanic.response import json, text
from sanic.log import logger
from requests import get
from sanic_jinja2 import SanicJinja2
import json as js
import os

app = Sanic(__name__)
jinja = SanicJinja2(app)
current_directory = os.path.dirname(os.path.abspath("application.py"))
static_directory = os.path.join(current_directory, 'static')
app.static('', static_directory)
search_data = {}

def filter_country_data(cy_data):
    for country in cy_data:
        search_data[country['alpha3Code']] = country
    logger.info(len(search_data))
    return search_data



@app.route("/")
async def countries(request):
    logger.info("Countries")
    cy_data = js.loads(get("https://restcountries.eu/rest/v2/all").text)
    # search_data = filter_country_data(cy_data)
    # print(search_data)
    return jinja.render("index.html", request, countries=cy_data)
    
if __name__ == "__main__":
    app.run(host="192.168.0.1", port=8000, debug=True)