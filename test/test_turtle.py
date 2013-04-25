from tiddlyweb.model.tiddler import Tiddler
from tiddlyweb.serializer import Serializer
from tiddlyweb.config import config

from tiddlywebplugins.rdf import init


def setup_module(module):
    config['server_host'] = {
        'scheme': 'http',
        'host': 'example.org',
        'port': '80',
    }
    config['server_prefix'] = '/wiki'
    module.ENVIRON = { 'tiddlyweb.config': config }

    init(config)


def test_entity():
    tiddler = Tiddler('Hello World', 'alpha')
    tiddler.fields["rdf:type"] = "skos:Concept"

    serializer = Serializer('tiddlywebplugins.rdf', ENVIRON)
    serializer.object = tiddler
    representation = serializer.to_string()

    assert representation == '''
@prefix : <http://example.org/wiki/>.
@prefix tweb: <http://tiddlyweb.com/>.

:bags/alpha/Hello%20World a tweb:tiddler, skos:Concept;
    tweb:bag :bags/alpha
    '''.strip()
