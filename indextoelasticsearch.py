from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'FirstName Lastname',
    'text': 'This is the best',
    'tags': 'hello, world',
    'timestamp': datetime.now(),
}
res = es.index(index="test", doc_type='doc', id=1, body=doc)

res = es.get(index="test", doc_type='doc', id=1)
print(res['_source'])

es.indices.refresh(index="test")
