from quart import Blueprint, render_template


bp_files = Blueprint(
    'bp_files',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static',
    url_prefix='/files'
)

@bp_files.route('/')
async def files():
    data = {
        'title': 'Files',
        'static': '/files/static'
    }
    return await render_template('files.pug', **data)
