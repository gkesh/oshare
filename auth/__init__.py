from quart import Blueprint, render_template


bp_auth = Blueprint(
    'bp_auth',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='assets',
    url_prefix='/auth'
)

@bp_auth.route('/login')
async def login():
    data = {
        'title': "Login"
    }
    return await render_template('login.pug', **data)

@bp_auth.route('/register')
async def register():
    data = {
        'title': "Register"
    }
    return await render_template('register.pug', **data)