from django.core.mail import EmailMessage
import re

class ContextRender:
	REGEX_PREFIX = re.compile(r'\{\% (.+?) \%\}', re.IGNORECASE)

	@staticmethod
	def closure(key):
		if isinstance(key, basestring):
			return r'{% ' + key + r' %}'
		return ''

	@classmethod
	def context_render(self, content, dict):
		keys = re.findall(self.REGEX_PREFIX, content)
		for key in keys:
			val = dict[key]
			regex = self.closure(key)
			regex = re.compile(regex)
			content = re.sub(regex, val, content)
		return content
