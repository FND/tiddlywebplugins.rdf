from tiddlyweb.serializations import SerializationInterface
from tiddlyweb.web.util import encode_name, server_host_url


def init(config):
    # register the serializer
    content_type = 'text/turtle'
    config['serializers'][content_type] = [__package__,
            '%s; charset=UTF-8' % content_type]
    config['extension_types']['turtle'] = content_type


class Serialization(SerializationInterface):

  def tiddler_as(self, tiddler):
    host = '%s%s/' % (server_host_url(self.environ),
        self.environ['tiddlyweb.config']['server_prefix']) # TODO: normalize -- XXX: reinventing the wheel?

    title, bag = [encode_name(name) for name in (tiddler.title, tiddler.bag)]
    return """
@prefix host: <%s>.
@prefix tweb: <http://tiddlyweb.com/>.

:bags/%s/%s a tweb:tiddler;
    tweb:bag :bags/%s
    """.strip() % (host, bag, title, bag)
