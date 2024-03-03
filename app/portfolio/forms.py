from django import forms


class ContactForm(forms.Form):
    email_sender_name = forms.CharField(
        required=True,
        max_length=255,
        label="Your Name",
    )
    email_sender_name.widget.attrs["class"] = "dark-form-field"

    email_subject = forms.CharField(
        required=True, max_length=255, label="Email Subject"
    )
    email_subject.widget.attrs["class"] = "dark-form-field"

    email_sender_email = forms.EmailField(required=True, label="Your Email")
    email_sender_email.widget.attrs["class"] = "dark-form-field"

    email_content = forms.CharField(
        required=True, min_length=10, widget=forms.Textarea, label="Email Content"
    )
    email_content.widget.attrs["class"] = "dark-form-field"
