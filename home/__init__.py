from quart import Blueprint, render_template


bp_home = Blueprint(
    'bp_home',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/home/static',
    url_prefix='/'
)

@bp_home.route('/')
async def home():
    data = {
        'title': 'Home',
        'static': '/home/static'
    }
    return await render_template('index.pug', **data)

@bp_home.route('/profile')
async def profile():
    data = {
        'title': '@gkesh',
        'user': {
            'uname': '@gkesh',
            'fname': 'Jikesh Thapa',
            'gender': 'M',
            'age': 24
        }
    }
    return await render_template('profile.pug', **data)