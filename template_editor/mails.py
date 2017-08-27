from django.core.mail import EmailMessage
from django.forms import model_to_dict
from template_editor.services import ContextRender
from open_course.models import Classroom, Teacher, Assistant
from template_editor.models import MailTemplate
import datetime

class EmailSender:
	@classmethod
	def send_message(self, title, content, targets, **context_dict):
		if ('title_dict' in context_dict):
			title = ContextRender.context_render(title, context_dict['title_dict'])
		if ('content_dict' in context_dict):
			content = ContextRender.context_render(content, context_dict['content_dict'])
		receivers = []
		if not isinstance(targets, list):
			receivers.append(targets)
		else:
			receivers = targets 
		email = EmailMessage(title, content, receivers)
		return email.send()

	@classmethod
	def invitation_letter(self, class_id, template_id):
		try:
			classroom = Classroom.objects.get(pk = class_id)
		except Classroom.DoesNotExist:
			raise Exception("Classroom not exist")

		try:
			template = MailTemplate.objects.get(pk = template_id):
		except 

		content = model_to_dict(classroom)
		targets = []

		if isinstance(classroom.start_date, datetime.date):
			content['start_date'] = classroom.start_date.isoformat()
		if isinstance(classroom.finish_date, datetime.date):
			content['finish_date'] = classroom.finish_date.isoformat()
		if isinstance(classroom.teacher, open_course.models.Teacher):
			content['teacher'] = classroom.teacher.name
			targets.append(classroom.teacher.topica_email)
		else:
			raise Exception("Teacher not exist")
		if isinstance(classroom.assistant, open_course.models.Assistant):
			content['assistant'] = classroom.assistant.name

		for key in content:
			if content[key] == None:
				content.pop(key)

		return send_message(template.title, template.context, targets, title_dict=content, content_dict=content)