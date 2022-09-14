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
    title = "Files"
    data = {
        'title': title,
        'static': "/files/static",
        'jtron': {
            'content': [
                """
                You can upload any type of file here and manipulate file present in the system. 
                Make sure to choose the right file, before uploading and avoid larger files (<50MB). 
                """,
                """
                Supported files include Audio (mp3, acc), Video (mkv, mp4), Image (jpeg, png, jpg), 
                Text (txt, json, yaml, pdf, docx) and some other select formats. Click the button 
                below for further details.
                """,
                """
                Make sure the type of the file is highlighted after the upload is complete.
                """
            ],
            'cta': "Learn More"
        }
    }
    return await render_template('files.pug', **data)
