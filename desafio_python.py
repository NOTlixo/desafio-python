import smtplib
import tkinter as tk


def enviar():
    try:
        email = email_entry.get()
        receiver_email= receiver_email_entry.get()

        assunto = assunto_entry.get()
        mensagem = mensagem_entry.get()

        text = f"assunto{assunto}\n\n{mensagem}"

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()

        server.login(email,"ovcd mqnx zcix ewcx")
        server.sendmail(email, receiver_email, text)


        print("email has been send to:" + receiver_email)

    except ValueError as e:
        print("erro",f"falha ao enviar o email: {e}")


#criando a janela
janela = tk.Tk()
janela.title("enviar email")
#caixa do email
email_entry= tk.Label(janela, text= "digite seu email:")
email_entry.pack()

email_entry= tk.Entry(janela)
email_entry.pack()

#caixa de quem vai receber o email
receiver_email_entry = tk.Label(janela,text=" digite o email de quem vai receber:")
receiver_email_entry.pack()

receiver_email_entry = tk.Entry(janela)
receiver_email_entry.pack()

# caixa do assunto
assunto_entry = tk.Label(janela, text=" digite o assunto do email:")
assunto_entry.pack()

assunto_entry = tk.Entry(janela)
assunto_entry.pack()

#caixa da mensagem
mensagem_entry = tk.Label(janela, text="digite sua mensagem:")
mensagem_entry.pack()

mensagem_entry = tk.Entry(janela)
mensagem_entry.pack()

#botão enviar
botao_enviar = tk.Button(janela, text="enviar", command= enviar)
botao_enviar.pack()
#inicia a aplicação
janela.mainloop()