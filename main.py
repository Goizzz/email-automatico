import smtplib
import email.message
from email.message import Message


gerente =str(input('qual o email do gerente?'))
gasto=int(input('Qual foi o gasto deste mês?'))
ganhos=int(input('Qual o faturamento deste mês?'))
if ganhos > gasto:
    lucro = ganhos - gasto

    corpo_email = f"""
    <p>Bom dia!</p>
    <p>Caro gerente, o lucro deste mês foi de:{lucro}</p>
                    """
    msg = email.message.Message()
    msg['Subject'] = "lucro mensal "
    msg['From'] = 'pedro.goismarques2004@gmail.com'

   

    msg['To'] = gerente
    password = 'gtctftvgpvpltqvz'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

else:
    prejuizo = gasto - ganhos
    corpo_email = f"""
        <p>Bom dia!</p>
        <p>Caro gerente, infelizmente esse mês tivemos um prejuizo de:{prejuizo}</p>
                        """
    msg = email.message.Message()
    msg['Subject'] = "prejuizo "
    msg['From'] = 'pedro.goismarques2004@gmail.com'

 

    msg['To'] = gerente
    password = 'gtctftvgpvpltqvz'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
