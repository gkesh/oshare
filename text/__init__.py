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
    title = "Text"
    data = {
        'title': title,
        'static': '/text/static',
        'jtron': {
            'content': [
                """
                You can upload links or text selections to be accessed by the laptop but be sure to avoid 
                super large texts, you can use the create file option if you wanna do something like that 
                but keep in mind that the text stored will not be formatted in any way.
                """,
                """
                When uploading texts, check if the proper type is highlighted, i.e. if an email is entered,
                an "@" tag will appear in the box. If the tagging does not appear, then the formatting must
                be wrong. For formatting information click the button below.
                """
            ],
            'cta': "Learn More"
        }
    }
    return await render_template('text.pug', **data)