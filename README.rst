django-naomi
============

Django-naomi is a email backend for Django that let you preview email from your web browser instead of sending it using SMTP server. This is perfect for development environment that lack of SMTP server or you want to debug the email message. This library is inspired from `Letter Opener <https://github.com/ryanb/letter_opener>`_.

Django Setup
------------

First, install django-naomi by using pip. You can add `django-naomi` to your requirements file or run this command. ::

    pip install django-naomi

Then, add `naomi` to your `INSTALLED_APPS` on your django settings file. ::

    INSTALLED_APPS += 'naomi'


Lastly, change the Django email backend and set the temporary directory. ::

    EMAIL_BACKEND = "naomi.mail.backends.naomi.NaomiBackend"
    EMAIL_FILE_PATH = "/home/test/tmp"


Please make sure that the `EMAIL_FILE_PATH` directory is writeable. That's all you need to do. Now, every time you send email it will shown on your web browser.

Development and Feedback
------------------------
Questions or problems? Please use the issue tracker. If you would like to contribute to this project, fork this repository and send me a pull request.
