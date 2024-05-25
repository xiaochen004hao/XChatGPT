t = "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"

import base64

t = t[3:]

t = bytes(t, encoding='utf-8')

_t = base64.b64encode(base64.b64encode(base64.b64encode(base64.b64encode(base64.b64encode(t)))))

t = str(b"sk-"+t, encoding='utf-8')

_t = str(_t, encoding='utf-8')

print(_t)

_t = bytes(_t, encoding='utf-8')

_t = base64.b64decode(base64.b64decode(base64.b64decode(base64.b64decode(base64.b64decode(_t)))))

_t = str(b"sk-"+_t, encoding='utf-8')

print(_t)

print(_t == t)
