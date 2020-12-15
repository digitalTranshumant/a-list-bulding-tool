#By Diego Saez-Trumper User:Diego(WMF)
#Try at  https://a-list-bulding-tool.toolforge.org/API/?wiki_db=enwiki&QID=Q82069695

from flask import request
import flask
import toolforge
from flask import jsonify

app = flask.Flask(__name__)

conn = toolforge.connect('wikidatawiki')
conn = toolforge.connect('wikidatawiki')


@app.route('/')
def index():
        return 'Use https://a-list-bulding-tool.toolforge.org/API/?wiki_db=enwiki&QID=Q82069695'


@app.route('/API/')
def APIRecs():
        conn = toolforge.connect('wikidatawiki')
        wiki_db = request.args.get('wiki_db', default ='enwiki')
        QID = request.args.get('QID')
        query =  """SELECT ips_site_page FROM wb_items_per_site WHERE 
                   ips_item_id in (SELECT SUBSTRING(page.page_title,2) FROM page WHERE page_id in 
                   (SELECT pl_from FROM pagelinks WHERE pl_title = '{}' AND 
                    pl_namespace = 0 AND pl_from_namespace = 0)) AND ips_site_id = '{}'""".format(QID,wiki_db)
        with conn.cursor() as cur:
                cur.execute(query)
                result = cur.fetchall()
        return jsonify([r[0].decode() for r in result])

