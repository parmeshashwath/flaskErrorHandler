from flask import request,jsonify
import inspect
import json
import datetime
import traceback
from collections import defaultdict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from multiprocessing import Pool


def send_email(message,usermailDetails):
    print("sending email....")
    sender= usermailDetails['from_addr']
    toaddr = usermailDetails['to_addr']

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    gmail_user = usermailDetails['from_addr']
    gmail_password = usermailDetails['password']
    server.login(gmail_user, gmail_password)


    msg = MIMEMultipart('alternative')
    msg['Subject'] =  " Error Notification "
    msg['From'] = sender
    msg['To'] = toaddr
    Message=email_body = json.dumps(message, indent=4, sort_keys=True).replace(' ', '&nbsp;').replace('\n', '<br>')


    part2 = MIMEText(Message,'html')
    msg.attach(part2)
    server.sendmail(sender,toaddr,msg.as_string())
    server.quit()
    print("mail send to "+toaddr )


class SafeRun(object):
    def safe_run(self,func,usermailDetails):

        def func_wrapper(*args, **kwargs):

            try:
                response =  func(*args, **kwargs)
            except Exception as e:
                print("unhandled Exception")
                print(e)
                data = {}
                traces = inspect.trace()
                temp = traces[-1][0]
                code = temp.f_code
                data['filename'] = code.co_filename
                data['functioncode'] = inspect.getsourcelines(code)[0]
                data['localvariables'] = temp.f_locals
                data['error_lineno'] = temp.f_lineno
                data['url'] = request.url
                data['function_start_lno'] = code.co_firstlineno
                data['stacktrace'] = traceback.format_exc().replace('\n','<br>')
                data['timestamp'] = str(datetime.datetime.now())
                pool = Pool(processes=1)
                result = pool.apply_async(send_email, [data,usermailDetails])
                # send_email(data,usermailDetails)
                response = jsonify({'result':'Something went wrong.Please try again..'}),500
            return response
        func_wrapper.__name__ = func.__name__
        return func_wrapper



    def checkMailCredentails(self,usermailDetails):
        try:

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            gmail_user = usermailDetails['from_addr']
            gmail_password = usermailDetails['password']
            server.login(gmail_user, gmail_password)
            return True
        except Exception as e:
            print("*************** Incorrect Mail Details Provided. *******************")
            print ("Module Not loaded...")
            return False

    def __init__(self, app,usermailDetails):
        if self.checkMailCredentails(usermailDetails):
            self.usermailDetails = usermailDetails
            with app.app_context():
                for name, func in app.view_functions.items():
                    app.view_functions[name] = self.safe_run(func,usermailDetails)
