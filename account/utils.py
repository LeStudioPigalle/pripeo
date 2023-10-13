from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings


def SendMailNewCard(informations):
    message = "Un nouveau client demande une carte ! \n\n Informations du client :\n\n- NOM : {last_name}\n- PRENOM : {first_name}\n- TEL : {phone}\n- EMAIL : {email}\n- PAYS : {pays}\n- LANGUE : {langage}\n\nSi vous désirez valider le dossier de ce client cliquez sur ce lien : https://app.pripeo.com/admin/account/account/{id}/change/.".format(**informations)
    mail = EmailMessage("Nouveau Client", message,f'"Support Pripeo" <{settings.EMAIL_HOST_USER}>', ['kaivsantatr@yahoo.fr'])

    carte_cni = str(informations['cni_image'])
    photo_selfie = str(informations['selfie'])

    mail.attach_file(carte_cni)
    mail.attach_file(photo_selfie)

    mail.send()


