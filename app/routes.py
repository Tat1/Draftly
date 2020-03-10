from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Miguel'}
    return'''
<HTML>
    <HEAD>
        <TITLE>Home Page -Draft</TITLE>
    </HEAD>
    <BODY>
        <H1>Draft</H1>
        <H2>Name your Story</H2>
        <H3>Choose your plotline</H3>
        <H3>Charcters</H3>
        <H3>Roles</H3>
    </BODY>
</HTML>'''
