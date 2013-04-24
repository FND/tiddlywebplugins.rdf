from tiddlyweb.serializations import SerializationInterface
from tiddlyweb.web.util import encode_name, server_host_url


def init(config):
    # register the serializer
    content_type = 'text/turtle'
    config['serializers'][content_type] = [__package__,
            '%s; charset=UTF-8' % content_type]
    config['extension_types']['turtle'] = content_type
