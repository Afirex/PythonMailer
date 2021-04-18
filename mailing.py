from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import smtplib, ssl
import sys


def mailer_util(body,sub,smtp_server,frm,passwd,to,cc='',attch='',bcc=''):

    rcpt=to.split(",")+ cc.split(",")


    message = MIMEMultipart('alternative')
    message['Subject'] = sub
    message['From'] = frm
    message['To'] = to
    message['Cc']=cc

    # body is received is CSV format-  for eg:  "Error 404 , Alert S5 , Description-file doesn't exist"   
    body=body.split(",")
    body2=""+body[1]
    body3=""+body[2]
    body=""+body[0]
    
    #wrapper can be modified as per requirement , you can use your own template here
    wrapper = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta charset="UTF-8"><meta content="width=device-width, initial-scale=1" name="viewport"><meta name="x-apple-disable-message-reformatting"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta content="telephone=no" name="format-detection"><title></title> <style type="text/css">a{text-decoration:none}</style><style>sup{font-size:100% }</style><![endif]--> <!--[if gte mso 9]> <xml> <o:OfficeDocumentSettings> <o:AllowPNG></o:AllowPNG> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> <![endif]--></head><body><div class="es-wrapper-color"> <!--[if gte mso 9]> <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" src="https://tlr.stripocdn.email/content/guids/CABINET_1934820098469b83c0d2c37274d71f41/images/88511610614983961.png" color="#141416" origin="0.5, 0" position="0.5, 0"></v:fill> </v:background> <![endif]--><table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0" background="https://tlr.stripocdn.email/content/guids/CABINET_1934820098469b83c0d2c37274d71f41/images/88511610614983961.png" style="background-position: center top;"><tbody><tr><td class="esd-email-paddings" valign="top"><table class="es-content esd-header-popover" cellspacing="0" cellpadding="0" align="center"><tbody><tr><td class="esd-stripe" align="center"><table class="es-content-body" style="background-color: transparent;" width="600" cellspacing="0" cellpadding="0" align="center"><tbody><tr><td class="esd-structure es-p10t es-p10r es-p10l" align="left" esd-custom-block-id="239121"><table width="100%" cellspacing="0" cellpadding="0"><tbody><tr><td class="es-m-p0r es-m-p20b esd-container-frame" width="580" valign="top" align="center"><table width="100%" cellspacing="0" cellpadding="0" bgcolor="#ff006e" style="background-color: #ff006e;"><tbody><tr><td align="center" class="esd-block-text es-p30t es-p20r es-p20l"><h1>"""+body+"""<br>"""+body2+"""</h1></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td class="esd-structure es-p40t es-p10r es-p10l" align="left" esd-custom-block-id="239122"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td width="580" class="esd-container-frame" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td align="left" class="esd-block-text es-m-txt-l"><h1 style="line-height: 120%;">"""+body2+"""</h1></td></tr><tr><td align="left" class="esd-block-text es-p10b"><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td class="esd-structure es-p40t es-p10r es-p10l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td width="580" class="esd-container-frame" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td align="left" class="esd-block-text es-p10b"><p>"""+body3+"""</p></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table><table cellpadding="0" cellspacing="0" class="esd-footer-popover es-footer" align="center"><tbody><tr><td class="esd-stripe" align="center"><table bgcolor="#ffffff" class="es-footer-body" align="center" cellpadding="0" cellspacing="0" width="600"><tbody><tr><td class="esd-structure es-p40t es-p10r es-p10l" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td width="580" class="esd-container-frame" align="center" valign="top"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td align="left" class="esd-block-text es-m-txt-l"><h1 style="line-height: 120%;">!!</h1></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td class="esd-structure es-p20" align="left" esd-custom-block-id="239128"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td width="560" class="esd-container-frame" align="left"><table cellpadding="0" cellspacing="0" width="100%"><tbody><tr><td align="center" class="esd-block-text es-p5t es-p5b"><p>This email was sent to&nbsp;<a target="_blank" href="mailto:your@mail.com">your@mail.com</a>.</p><p>You are receiving this email because you have visited our site or asked us about regular newsletter.</p></td></tr><tr><td align="center" class="esd-block-text es-p5t es-p5b"><p><a target="_blank" href="https://viewstripo.email">Unsubscribe</a>&nbsp;from future emails.</p></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table></div></body></html>"""
    email_template = wrapper 
    

                            
    message.attach(MIMEText(body, 'plain'))
    message.attach(MIMEText(email_template,'html'))
   
    ''' Attaching multiple files '''
    
    if attch!='':
        attch=attch.split(",")
        for x in attch:
            filename = x
            attachName=x
            with open(filename, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            encoders.encode_base64(part)

            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachName}",
                )
            message.attach(part)

    ctx=ssl.create_default_context()
    
    server = smtplib.SMTP(smtp_server,587) #smtplib.SMTP(smtp_server, 995) for IMAP ## FOLLOW  UP
    server.ehlo()
    server.starttls()
    server.ehlo
    server.login(message['From'], passwd)
    server.sendmail(message['From'],rcpt, message.as_string())
    server.quit()


if __name__ == '__main__':
    print("\n\n",sys.argv,"\n\n")
    if len(sys.argv)<7:
        print("Params missing")
    elif len(sys.argv)==7:
        mailer_util(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6])
    elif len(sys.argv)==8:
        mailer_util(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],
                    sys.argv[6],sys.argv[7])
    elif len(sys.argv)==9:
        mailer_util(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],
                    sys.argv[6],sys.argv[7],sys.argv[8])
    else:
        print("Check Parameters")


#----------------------------------------------------------------
#        
#   Command format :
#
#   python mailing.py "Error XXX, Alert LEVEL,Description here" "Subject Here" "smtp server here" "From@mail.com" "PasswordHere" "to@gmail.com" "ccc@gmail.com,cc@mail.com" "attachment path 1, attachment path 2"
#
#   if no attachment or CC contacts // it can be skipped from command 
#
#   For gmail use :smtp.gmail.com // you might have to allow less secure apps from here : https://myaccount.google.com/lesssecureapps
#   For outlook use : smtp.office365.com
#
# ---------------------------------------------------------------
