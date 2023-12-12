# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )

    """
        The author field has the forms.TextInput widget. This tells Django to load this field as an HTML text input element in the templates. The body field uses a forms.TextArea widget instead, so the field is rendered as an HTML text area element.

        These widgets also take the argument attrs, which is a dictionary that allows you to specify some CSS classes
    """

    """
    Once you’ve created the Django form for comments, have a look at how a form travels through requests:

    When a user visits a page containing a form, they send a GET request to the server. In this case, there’s no data entered in the form, so you just want to render the form and display it.
    When a user enters information and clicks the Submit button, they send a POST request, containing the data submitted with the form, to the server. At this point, the data goes for processing, and two things can happen:
    1. The form is valid, and the user is redirected to the next page.
    2. The form is invalid, and the empty form shows up once again. The user is back at step 1, and the process repeats.
    """