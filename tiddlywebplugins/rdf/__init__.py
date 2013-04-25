from tiddlyweb.serializations import SerializationInterface
from tiddlyweb.web.util import encode_name, server_base_url


def init(config):
    # register the serializer
    content_type = 'text/turtle'
    config['serializers'][content_type] = [__package__,
            '%s; charset=UTF-8' % content_type]
    config['extension_types']['turtle'] = content_type


class Serialization(SerializationInterface):

  def tiddler_as(self, tiddler):
    host = '%s/' % server_base_url(self.environ) # TODO: normalize?

    title, bag = [encode_name(name) for name in (tiddler.title, tiddler.bag)]

    namespaces = {
        '': host,
        'tweb': 'http://tiddlyweb.com/'
    }
    subject = ':bags/%s/%s' % (bag, title)
    rdf_data = {
        subject: {
            'rdf:type': ['tweb:tiddler'],
            'tweb:bag': [':bags/%s' % bag]
        }
    }

    for field, value in tiddler.fields.items():
        try:
            prefix, suffix = field.split(':')
            # TODO: use collections.defaultdict
            rdf_data[subject] = rdf_data[subject] or {}
            rdf_data[subject][field] = rdf_data[subject][field] or []
            rdf_data[subject][field].append(value)
        except ValueError: # not RDF-related
            pass

    return to_turtle(namespaces, rdf_data)


def to_turtle(namespaces, rdf_data):
    headers = ['@prefix %s: <%s>.' % (name, uri) for name, uri
            in namespaces.items()]

    triples = []
    for rdf_sbj, subject_data in rdf_data.items():
        fields = ['%s %s' % (resolve_predicate(rdf_prd), ', '.join(rdf_objects))
                for rdf_prd, rdf_objects in subject_data.items()]
        fields = '%s %s' % (rdf_sbj, ';\n    '.join(fields))
        triples.append(fields)

    return '\n'.join(headers + [''] + triples)


def resolve_predicate(prd):
    return 'a' if prd == 'rdf:type' else prd
