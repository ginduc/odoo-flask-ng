from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms import validators

from sd5.models import User, Recipient


class LoginForm(Form):
    username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.optional()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # Does our the exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False

        return True


class RecipientForm(Form):
    firstname = TextField(u'First Name', validators=[validators.required()])
    lastname = TextField(u'Last Name', validators=[validators.required()])
    mobileNo = TextField(u'Mobile No', validators=[validators.required()])
    address = TextAreaField(u'Address', validators=[validators.optional()])

    def validate(self):
        check_validate = super(RecipientForm, self).validate()

        if not check_validate:
            return False

        # Check if recipient name exists already

        # Check if mobile no exists already

        return True

    def to_model(self):
        return Recipient(self.firstname.data, self.lastname.data,
                         self.mobileNo.data, self.address.data)
