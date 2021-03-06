"""
Create A New Exception Example:
```
    class BarException(AppException):
        message = "This Is A Sample Error text"
        status_code = 423
        code = 1025
```

Usage of created exception in Views Example:
```
    from application import exc
    @app.route('/foo')
    def get_foo():
        raise exc.BarException
```
"""

class ApplicationException(Exception):
    status_code = 400
    message =  "Empty"
    payload = {}

    def __init__(self):
        Exception.__init__(self)

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


class EmptyForm(ApplicationException):
    status_code = 701
    message = '400 Empty Form'


class EmailNotInForm(ApplicationException):
    status_code = 702
    message = '400 Email Not In Form'


class PasswordNotInForm(ApplicationException):
    status_code = 703
    message = '400 Password Not In Form'


class FullnameNotInForm(ApplicationException):
    status_code = 704
    message = '400 Fullname Not In Form'


class DuplicateMemberFound(ApplicationException):
    status_code = 705
    message = '400 Member Already Exists'


class MemberNotFound(ApplicationException):
    status_code = 706
    message = '401 Member Not Found'


class MemberIdNotInForm(ApplicationException):
    status_code = 707
    message = '400 Member Id Not In Form'


class TargetWithYourselfError(ApplicationException):
    status_code = 707
    message = '400 Target With Yourself Error'

