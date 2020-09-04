dev=True
if dev:
	from .development import *
else:
	from .production import *