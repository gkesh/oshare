from quart import Quart

from home import bp_home
from files import bp_files
from text import bp_text
from auth import bp_auth


app = Quart(
    __name__, 
    static_folder="static",
    static_url_path="/static"
)
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')

app.register_blueprint(bp_home)
app.register_blueprint(bp_files)
app.register_blueprint(bp_text)
app.register_blueprint(bp_auth)
