import datetime
import os
from django.core.mail.backends.filebased import EmailBackend
import webbrowser
from django.template.loader import render_to_string


class NaomiBackend(EmailBackend):
    """
    """

    def write_message(self, message):
        template_content = render_to_string('naomi/message.html', {'message': message})
        self.stream.write(template_content)

    def _get_filename(self):
        """Return a unique file name."""
        if self._fname is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            fname = "%s-%s.html" % (timestamp, abs(id(self)))
            self._fname = os.path.join(self.file_path, fname)
            webbrowser.open(self._fname)
        return self._fname
