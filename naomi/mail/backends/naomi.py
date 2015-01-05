import datetime
import os
import six
import webbrowser
from django.core.mail.backends.filebased import EmailBackend
from django.template.loader import render_to_string


class NaomiBackend(EmailBackend):
    """
    Email backend for Django that let you preview email on your web browser
    """

    def __init__(self, *args, **kwargs):
        super(NaomiBackend, self).__init__(*args, **kwargs)

    def write_message(self, message):
        if hasattr(message, 'alternatives') and message.alternatives:
            body = message.alternatives[0][0]
        else:
            body = message.body
        template_content = render_to_string('naomi/message.html', {'message': message, 'body': body})
        if six.PY3:
            self.stream.write(bytes(template_content, 'UTF-8'))
        else:
            self.stream.write(template_content)

    def _get_filename(self):
        """Return a unique file name."""
        if self._fname is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fname = "%s-%s.html" % (timestamp, abs(id(self)))
            self._fname = os.path.join(self.file_path, fname)
            webbrowser.open(self._fname)
        return self._fname

    def send_messages(self, email_messages):
        """Write all messages to the stream in a thread-safe way."""
        if not email_messages:
            return
        with self._lock:
            try:
                stream_created = self.open()
                for message in email_messages:
                    if six.PY3:
                        self.write_message(message)
                    else:
                        self.write_message(message)
                    self.stream.flush()
                if stream_created:
                    self.close()
            except:
                if not self.fail_silently:
                    raise
        return len(email_messages)
