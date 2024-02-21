import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

"""# ver idiomas
engine = pyttsx3.init()
for voz in engine.getProperty('voices'):
    print(voz)"""

# opciones de voz/idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


# escuchar microfono y devolver audio como texto
def transformar_audio_en_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comienza a grabar
        print('Ya puedes hablar')

        # guardar lo escuchado com audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-es")

            # prueba ingreso
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprende el audio
            print('no hay servicio')
            # devolver error
            return 'sigo esperando'
        # en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprende el audio
            print('no entendí')
            # devolver error
            return 'sigo esperando'
        # error inesperado
        except:
            # prueba de que no comprende el audio
            print('algo ha salido mal')
            # devolver error
            return 'sigo esperando'


# transformar el texto del asistente en voz
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar dia semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # variable dia semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # decir dia semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar hora
def pedir_hora():
    # crear variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} horas con {hora.minute} minutos'

    # decir hora
    hablar(hora)


# saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"
    # decir saludo
    hablar(f'{momento} soy Friday.Tu asistente personal. En qué puedo ayudarte')


# funcion central del asistente
def pedir_cosas():
    # activar saludo
    saludo_inicial()

    # variable de corte
    comenzar = True
    # loop central
    while comenzar:
        # activar micro y guardar en string
        pedido = transformar_audio_en_texto().lower()

        if 'youtube' in pedido:
            hablar('estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'navegador' in pedido:
            hablar('Estoy en ello')
            webbrowser.open('https://www.google.es')
            continue
        elif 'gracias' in pedido:
            hablar('De nada simpática')
            continue
        elif 'netflix' in pedido:
            hablar('claro que sí, guapi')
            webbrowser.open('https://www.netflix.com')
            continue
        elif 'qué día' in pedido:
            pedir_dia()
            continue
        elif 'qué hora' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('buscando lo que no sabes en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('wikipedia dice:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Marchando')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproduce' in pedido:
            hablar('Qué buen gusto musical')
            pedido = pedido.replace('reproduce', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL',
                       'amazon': 'AMZN',
                       'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada).info
                precio_actual = accion_buscada['regularMarketPreviousClose']
                hablar(f'La encontré. El precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Pero qué me estás contando')
                continue
        elif 'adiós' in pedido:
            hablar('que te cunda')
            break


pedir_cosas()
