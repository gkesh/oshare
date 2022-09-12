from quart import Blueprint, render_template


bp_text = Blueprint(
    'bp_text',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
    url_prefix='/text'
)

@bp_text.route('/')
async def text():
    data = {
        'title': 'Text',
        'static': '/text/static'
    }
    return await render_template('text.pug', **data)