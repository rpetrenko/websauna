import deform
import deform.widget as w
import colander as c


from hem.schemas import CSRFSchema
from .models import _
from horus.schemas import unique_email

PASSWORD_MIN_LENGTH = 6


class RegisterSchema(CSRFSchema):
    """Username-less registration form schema."""

    email = c.SchemaNode(
        c.String(),
        title=_('Email'),
        validator=c.All(c.Email(), unique_email),
        widget=w.TextInputWidget(size=40, maxlength=260, type='email'))

    password = c.SchemaNode(
        c.String(),
        validator=c.Length(min=PASSWORD_MIN_LENGTH),
        widget=deform.widget.CheckedPasswordWidget(),
    )


class LoginSchema(CSRFSchema):
    """Login form schema."""

    email = c.SchemaNode(c.String(), title=_('Email'), validator=c.All(c.Email(), unique_email), widget=w.TextInputWidget(size=40, maxlength=260, type='email'))

    password = c.SchemaNode(c.String(), validator=c.Length(min=PASSWORD_MIN_LENGTH), widget=deform.widget.PasswordWidget())