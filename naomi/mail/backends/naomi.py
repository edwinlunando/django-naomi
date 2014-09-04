import datetime
import os
import webbrowser
from django.core.mail.backends.filebased import EmailBackend
from django.template.loader import render_to_string


class NaomiBackend(EmailBackend):
    """
    Email backend for Django that let you preview email on your web browser
    """

    def write_message(self, message):
        body = message.alternatives[0][0]
        template_content = render_to_string('naomi/message.html', {'message': message, 'body': body})
        self.stream.write(template_content)

    def _get_filename(self):
        """Return a unique file name."""
        if self._fname is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fname = "%s-%s.html" % (timestamp, abs(id(self)))
            self._fname = os.path.join(self.file_path, fname)
            webbrowser.open(self._fname)
        return self._fname
