from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
import smtplib
import sys


def mailer_util(body,sub,smtp_server,frm,passwd,to,cc='',attch='',bcc=''):

    rcpt=to.split(",")+ cc.split(",")


    message = MIMEMultipart('alternative')
    message['Subject'] = sub
    message['From'] = frm
    message['To'] = to
    message['Cc']=cc


    wrapper = """<html>
    <head>
    <title></title>
    </head>
    <body><h1>%s <p>MeowInWraaper</p><p></h1>URL: %s </p><h2>%s</h2></body>
    </html>"""

    email_template = wrapper % (body, 'now', 'url')

                            
    message.attach(MIMEText(body, 'plain'))
    message.attach(MIMEText(email_template,'html'))
   
    ''' Attaching multiple files '''
    
    if attch!=['']:
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

    
    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(message['From'], passwd)
    server.sendmail(message['From'],rcpt, message.as_string())
    server.quit()


if __name__ == '__main__':
    
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
    
#mailer_util("bodyWork Done by AFtab","Trying attachments","smtp.gmail.com","axnu@gmail.com",'XXX123XXX',
#            ['SEAA@gmail.com','SEFF@gmail.com'],
#            ['SEDD@gmail.com'],["C:/Users/DELL/OneDrive/Desktop/lemonsoda.txt","C:/Users/DELL/OneDrive/Desktop/AUTOSYS.png"])
#mailer_util(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],
#                    sys.argv[6],["REDD@gmail.com"],["C:/Users/DELL/OneDrive/Desktop/lemonsoda.txt","C:/Users/DELL/OneDrive/Desktop/AUTOSYS.png"])



#Params Accepted: (message body, Subject , smtpservice , from , password , to , cc , attach ,bcc )

#ex: python mailing.py '<h1>LoChicken</h2>' 'MessageOPEN SUbject' 'smtp.gmail.com' 'SSS@gmail.com' 'passwordLolminex221' 'SSS@gmail.com'
# 'cucs@gmail.com,ammad@gmail.com' 'C:/Users/DELL/OneDrive/Desktop/AUTO.png,C:/Users/DELL/OneDrive/Desktop/lemonsoda.txt'

#MULTIPLE TO,CC can be given as csv  eg: "lol@xxx.com,koi@xxx.com"










'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart('alternative')
message['Subject'] = 'Important'
message['From'] = 'QWE@gmail.com'
message['To'] = 'QWE@gmail.com'
cc='QWE@gmail.com'
message['Cc']=cc
message.attach(MIMEText('# A Heading\nSomething else in the body', 'plain'))
message.attach(MIMEText('<h1 style="color: RED">A Heading</h1><h2>lol</h2><p>Something else in the body</p>', 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(message['From'], 'SSSSSPASSW')
server.sendmail(message['From'], [message['To'],cc], message.as_string())
server.quit()

'''


'''
  message.attach(MIMEText("""<!DOCTYPE html><html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"><head>
              <meta charset="utf-8">
              <meta name="viewport" content="width=device-width,initial-scale=1">
              <meta name="x-apple-disable-message-reformatting">
              <title></title>
                    <!--[if mso]>
              <style>
                table {border-collapse:collapse;border-spacing:0;border:none;margin:0;}
                div, td {padding:0;}
                div {margin:0 !important;}
                    </style>
              <noscript>
                <xml>
                  <o:OfficeDocumentSettings>
                    <o:PixelsPerInch>96</o:PixelsPerInch>
                  </o:OfficeDocumentSettings>
                </xml>
              </noscript>
              <![endif]-->
              <style>
                table, td, div, h1, p {
                  font-family: Arial, sans-serif;
                }
                @media screen and (max-width: 530px) {
                  .unsub {
                    display: block;
                    padding: 8px;
                    margin-top: 14px;
                    border-radius: 6px;
                    background-color: #555555;
                    text-decoration: none !important;
                    font-weight: bold;
                  }
                  .col-lge {
                    max-width: 100% !important;
                  }
                }
                @media screen and (min-width: 531px) {
                  .col-sml {
                    max-width: 27% !important;
                  }
                  .col-lge {
                    max-width: 73% !important;
                  }
                }
              </style>
            </head>
        <body style="margin:0;padding:0;word-spacing:normal;background-color:#939297;">
    <div role="article" aria-roledescription="email" lang="en" style="text-size-adjust:100%;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;background-color:#939297;">
                <table role="presentation" style="width:100%;border:none;border-spacing:0;">
                  <tr>
                    <td align="center" style="padding:0;">
                      <!--[if mso]>
                      <table role="presentation" align="center" style="width:600px;">
                      <tr>
                      <td>
                      <![endif]-->
        <table role="presentation" style="width:94%;max-width:600px;border:none;border-spacing:0;text-align:left;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                        <tr>
                          <td style="padding:40px 30px 30px 30px;text-align:center;font-size:24px;font-weight:bold;">
                            <a href="http://www.example.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/logo.png" width="165" alt="Logo" style="width:80%;max-width:165px;height:auto;border:none;text-decoration:none;color:#ffffff;"></a>
                          </td>
                        </tr>
                        <tr>
                          <td style="padding:30px;background-color:#ffffff;">
        <h1 style="margin-top:0;margin-bottom:16px;font-size:26px;line-height:32px;font-weight:bold;letter-spacing:-0.02em;">{{body}}</h1>
        
                            <p style="margin:0;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In tempus adipiscing felis, sit amet blandit ipsum volutpat sed. Morbi porttitor, <a href="http://www.example.com/" style="color:#e50d70;text-decoration:underline;">eget accumsan dictum</a>, nisi libero ultricies ipsum, in posuere mauris neque at erat.</p>
                          </td>
                        </tr>
                        <tr>
                          <td style="padding:0;font-size:24px;line-height:28px;font-weight:bold;">
                            <a href="http://www.example.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/1200x800-2.png" width="600" alt="" style="width:100%;height:auto;display:block;border:none;text-decoration:none;color:#363636;"></a>
                          </td>
                        </tr>
                        <tr>
                          <td style="padding:35px 30px 11px 30px;font-size:0;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                            <!--[if mso]>
                            <table role="presentation" width="100%">
                            <tr>
                            <td style="width:145px;" align="left" valign="top">
                            <![endif]-->
                            <div class="col-sml" style="display:inline-block;width:100%;max-width:145px;vertical-align:top;text-align:left;font-family:Arial,sans-serif;font-size:14px;color:#363636;">
                              <img src="https://assets.codepen.io/210284/icon.png" width="115" alt="" style="width:80%;max-width:115px;margin-bottom:20px;">
                            </div>
                            <!--[if mso]>
                            </td>
                            <td style="width:395px;padding-bottom:20px;" valign="top">
                            <![endif]-->
                            <div class="col-lge" style="display:inline-block;width:100%;max-width:395px;vertical-align:top;padding-bottom:20px;font-family:Arial,sans-serif;font-size:16px;line-height:22px;color:#363636;">
                              <p style="margin-top:0;margin-bottom:12px;">Nullam mollis sapien vel cursus fermentum. Integer porttitor augue id ligula facilisis pharetra. In eu ex et elit ultricies ornare nec ac ex. Mauris sapien massa, placerat non venenatis et, tincidunt eget leo.</p>
                              <p style="margin-top:0;margin-bottom:18px;">Nam non ante risus. Vestibulum vitae eleifend nisl, quis vehicula justo. Integer viverra efficitur pharetra. Nullam eget erat nibh.</p>
                              <p style="margin:0;"><a href="https://example.com/" style="background: #ff3884; text-decoration: none; padding: 10px 25px; color: #ffffff; border-radius: 4px; display:inline-block; mso-padding-alt:0;text-underline-color:#ff3884"><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%;mso-text-raise:20pt">&nbsp;</i><![endif]--><span style="mso-text-raise:10pt;font-weight:bold;">Claim yours now</span><!--[if mso]><i style="letter-spacing: 25px;mso-font-width:-100%">&nbsp;</i><![endif]--></a></p>
                            </div>
                            <!--[if mso]>
                            </td>
                            </tr>
                            </table>
                            <![endif]-->
                          </td>
                        </tr>
                        <tr>
                          <td style="padding:30px;font-size:24px;line-height:28px;font-weight:bold;background-color:#ffffff;border-bottom:1px solid #f0f0f5;border-color:rgba(201,201,207,.35);">
                            <a href="http://www.example.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/1200x800-1.png" width="540" alt="" style="width:100%;height:auto;border:none;text-decoration:none;color:#363636;"></a>
                          </td>
                        </tr>
                        <tr>
                          <td style="padding:30px;background-color:#ffffff;">
                            <p style="margin:0;">Duis sit amet accumsan nibh, varius tincidunt lectus. Quisque commodo, nulla ac feugiat cursus, arcu orci condimentum tellus, vel placerat libero sapien et libero. Suspendisse auctor vel orci nec finibus.</p>
                          </td>
                        </tr>
                        <tr>
                          <td style="padding:30px;text-align:center;font-size:12px;background-color:#404040;color:#cccccc;">
                            <p style="margin:0 0 8px 0;"><a href="http://www.facebook.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/facebook_1.png" width="40" height="40" alt="f" style="display:inline-block;color:#cccccc;"></a> <a href="http://www.twitter.com/" style="text-decoration:none;"><img src="https://assets.codepen.io/210284/twitter_1.png" width="40" height="40" alt="t" style="display:inline-block;color:#cccccc;"></a></p>
                            <p style="margin:0;font-size:14px;line-height:20px;">&reg; Someone, Somewhere 2021<br><a class="unsub" href="http://www.example.com/" style="color:#cccccc;text-decoration:underline;">Unsubscribe instantly</a></p>
                          </td>
                        </tr>
                      </table>
                      <!--[if mso]>
                      </td>
                      </tr>
                      </table>
                      <![endif]-->
                    </td></tr></table></div></body></html>""",
                            'html'))
'''
