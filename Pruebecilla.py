#!/usr/bin/python3 -u
import telebot
import time
import urllib
import subprocess

import os


from telebot import types

bot = telebot.TeleBot('Aqui va la direccion que nos de BotFather')
tiempo = time.strftime("%H horas %M minutos y %S segundos exactamente")
#sti = open('/tmp/sti.webp', 'bot')
cat='http://www.wallpapersis.com/wp-content/uploads/2013/09/Stretches-White-Feet-Eyes-Cover-Blanket-Kitty-Cat.jpg'
f = open('out.jpg','wb')
f.write(urllib.request.urlopen(cat).read())
f.close()

@bot.message_handler(commands=['start'])
def send_photo(message):
    bot.send_message(message.chat.id, 'Este es su asistente personal. Puede preguntarme por su horario y que le mande un examen de la constitución española. \n Cuando no entiendo algo, lo repito. ')

def recibe(messages):
    for m in messages:
        if m.content_type == "text":
            if m.text == "Hola":
                bot.send_message(m.chat.id,"Hola")
                bot.send_message(m.chat.id,"\n¿Como estas?")
            elif m.text == "puedo llamarte al?":
                bot.send_message(m.chat.id,"me la pela")
            elif m.text == "te gusta el rock?":
                bot.send_message(m.chat.id,"no tengo gustos, señor")
                bot.send_message(m.chat.id,"Lo siento")
            elif m.text == "id":
                bot.send_message(m.chat.id,"158424035:AAFS-MVS0dukkgNOdzr4cLLeERE-ub-gcto")
                bot.send_message(m.chat.id,"cuidado con mi código, por favor...")
            elif m.text == "Tontopollas":
                bot.send_message(m.chat.id,"Que dise")
                bot.send_message(m.chat.id,"Que te reviento")
                bot.send_message(m.chat.id,"Payaso")
            elif m.text == "hora?":
                bot.send_message(m.chat.id,"Son las "+tiempo+" señor")
            #elif m.text == "gracias":
             #   bot.send_sticker(m.chat.id, sti)

            elif m.text == "Clases":
                bot.send_message(m.chat.id,"Lunes: DDSI y MC, Martes: IG y MC,  Miércoles: FR y IG ,Jueves: ISE y FR, Viernes: DDSI y ISE ")
                bot.send_message(m.chat.id,"Si quiere más detalles, dígame qué día es hoy")
            elif m.text == "Lunes":
                bot.send_message(m.chat.id,"Hoy tiene 1 hora de DDSI de prácticas 3.5, 1 hora de DDSI de teoría y 2 horas de MC prácticas 2.2")
            elif m.text == "Martes":
                bot.send_message(m.chat.id,"Hoy tiene 2 horas de IG de prácticas 3.3 y 2 horas de MC de teoría 1.1")
            elif m.text == "Miercoles":
                bot.send_message(m.chat.id,"Hoy tiene 2 horas de FR de prácticas 3.7 o 0.1 y 2 horas de IG de teoría 0.4")
            elif m.text == "Jueves":
                bot.send_message(m.chat.id,"Hoy tiene 2 horas de ISE de prácticas 2.3 y 2 horas de FR de teoría 1.1")
            elif m.text == "Viernes":
                bot.send_message(m.chat.id,"Hoy tiene 2 horas de DDSI de prácticas 3.3 y 2 horas de ISE de teoría 1.1")
            elif m.text == "gracias":
                bot.send_message(m.chat.id,"Para servirle, señor")
            elif m.text == "ayuda":
                bot.send_message(m.chat.id,"puede preguntar por: 'clases' saludar, decir el día de la semana preguntar la hora 'hora?' o mi id 'id' o pedir la foto de un gato 'gatete'. Escriba siempre en minúscula. Cuando no entiendo algo, lo repito ")
            # elif m.text == "foto":
            #     bot.send_chat_action(m.chat.id, 'upload_photo')
            #     img = open('out.jpg', 'rb')
            #     bot.send_photo(m.chat.id, img, reply_to_message_id=m.message_id)
            #     img.close()
            elif m.text == "Archivos":
                resultado = subprocess.getoutput("ls")
                bot.send_message(m.chat.id, resultado)
            elif m.text == "Ejecuta":
                resultado = subprocess.getoutput("python3 hola.py")
                bot.send_message(m.chat.id, resultado)
            elif m.text == "Examen":
                os.system('./Examen/bin/pruebagen_test ./datos/PreguntasConstitucion.txt ./datos/examen.tex 10')
                os.system('make -C ./Examen/datos')
                doc = open('./Examen/Examen.pdf', 'rb') # Es la función equivalente a enviar un archivo desde telegram.
                bot.send_document(m.chat.id, doc)
            elif m.text == "dime":
                bot.send_message(m.chat.id,"No he dicho nada")


            else:
                bot.send_message(m.chat.id,m.text)


bot.set_update_listener(recibe)

bot.polling()
