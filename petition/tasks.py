from textwrap import wrap

from celery import shared_task
from mail_templated import EmailMessage

import io
import csv


@shared_task
def send_signature_verification_email(token, sender, receiver, full_name):
    email = EmailMessage(
        template_name="email/signature_verification.tpl",
        from_email=sender,
        to=[receiver],
        context={
            "token": token,
            "full_name": full_name,
        },
    )
    email.send()


def csv_generator(data):
    output_file = io.StringIO()
    cr = csv.writer(output_file, delimiter=",")
    cr.writerow(["First_name", "Last_name", "email", "Country"])
    for sgn in data:
        cr.writerow(sgn)
    output_file.seek(0)
    return output_file.getvalue()


@shared_task
def send_successful_petition_report(data):
    email = EmailMessage(
        template_name="email/successful_petition_report.tpl",
        from_email="petition_report@plea.org",
        to=[data.get("petition_recipient_email")],
        context={
            "title": data.get("petition_title"),
            "owner": data.get("petition_owner_name"),
            "recipient_name": data.get("petition_recipient_name"),
            "goal": data.get("petition_goal"),
        },
    )
    csv_file = csv_generator(data=data.get("petition_signatures"))
    email.attach("report.csv", csv_file, "text/csv")
    email.send()


@shared_task
def send_successful_petition_report_to_signers(data):
    email = EmailMessage(
        template_name="email/successful_petition_report_to_signers.tpl",
        from_email="petition_report@plea.org",
        to=data.get("let_signers_know"),
        context={
            "title": data.get("petition_title"),
            "owner": data.get("petition_owner_name"),
            "goal": data.get("petition_goal"),
        },
    )
    email.send()
