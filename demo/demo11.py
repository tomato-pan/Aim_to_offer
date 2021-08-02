from typing import Dict, Any
from emails.template import JinjaTemplate
import requests
import emails

def send_email(
    email_to: str,
    subject_template: str = "",
    html_template: str = ""
) -> None:
    # assert False, "no provided configuration for email variables"
    message = emails.Message(
        subject=JinjaTemplate(subject_template),
        html=JinjaTemplate(html_template),
        mail_from=("panj", "pj_uestc@163.com"),
    )
    smtp_options = {"host": "smtp.163.com","timeout":120}
    response = message.send(to=email_to, smtp=smtp_options)
    print(f"send email result: {response}")
    print(response.status_code)


def send_test_email(email_to: str) -> None:
    project_name = "test"
    subject = f"{project_name} - Test email"
    with open( "test_email.html") as f:
        template_str = f.read()
        # print(template_str)
    send_email(
        email_to=email_to,
        subject_template=subject,
        html_template=template_str
    )
if __name__ == '__main__':
    send_test_email("panj@wangsu.com")
