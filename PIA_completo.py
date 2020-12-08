#PIA
#JUAN MANUEL LOPEZ TORRES
#CHRISTOPHER JAIR ESCAMILLA GARCIA

import nmap
import shodan
import socket
from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
import os
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import hashlib
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import argparse
parser = argparse.ArgumentParser()
parser.parse_args()
parser.add_argument("echo", help="echo the string you use here")

def todos_juntos():
    
    uno = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\scrp_hash_512.txt' , 'r' , errors='ignore').readlines()
    dos = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\puert_hash_512.txt' , 'r' , errors='ignore').readlines()
    tre = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\meta_hash_512.txt' , 'r' , errors='ignore').readlines()
    cua = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\meta.txt' , 'r' , errors='ignore').readlines()
    cin = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\clavesHASH-scraping.txt' , 'r' , errors='ignore').readlines()
    six = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\clavesHASH-meta.txt' , 'r' , errors='ignore').readlines()
    sev = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\clavesHASH-puertos.txt' , 'r' , errors='ignore').readlines()
    och = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\API_shodan_hash_512.txt' , 'r' , errors='ignore').readlines()

    uno = list(map(str.strip, uno))
    dos = list(map(str.strip, dos))
    tre = list(map(str.strip, tre))
    cua = list(map(str.strip, cua))
    cin = list(map(str.strip, cin))
    six = list(map(str.strip, six))
    sev = list(map(str.strip, sev))
    och = list(map(str.strip, och))
    fic = open('Reporte_general.txt', 'w')
    fic.write("los hash de webScraping de texto")
    fic.write('\n')
    fic.write('\n')
    for i in uno :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Los hash de los puerto abiertos")
    fic.write('\n')
    fic.write('\n')
    for i in dos :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Los Hash de la metadata de las imagenes")
    fic.write('\n')
    fic.write('\n')
    for i in tre :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Las metadata")
    fic.write('\n')
    fic.write('\n')
    for i in cua :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Las claves hash y su respectivo scraping")
    fic.write('\n')
    fic.write('\n')
    for i in cin :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Las claves hash y su respectiva Metadata")
    fic.write('\n')
    fic.write('\n')
    for i in six :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Las claves Hash y su respectivo puerto")
    fic.write('\n')
    fic.write('\n')
    for i in sev :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.write("Las claves hash de los host")
    fic.write('\n')
    fic.write('\n')
    for i in och :
        fic.write(i)
        fic.write('\n')
    fic.write('\n')
    fic.write('\n')
    fic.close()

#--------------------------------------------------------------------------------------
def escaneo_puertos():
    print ("Escaneando puertos:................")
    begin = 83
    end = 85
    target = '148.234.5.206'

    scan= nmap.PortScanner()
    fic = open('puertos.txt', 'w')
    sites = []
    api_key = "qbHgFeeyIwVq55pNH20ycSNuIiyc5pDO"
    objeto = shodan.Shodan(api_key)
    resultados = objeto.search("SMTP")
    print("numero de host encontrados: ", len(resultados['matches']))
    for match in resultados['matches']:
        if match['ip_str'] is not None:
            print(match['ip_str'])
            sites.append(match['ip_str'])
    mom = open('API_shodan.txt', 'w')
    for i in sites:
        mom.write(i)
        mom.write("\n")
    mom.close()

    for i in range(begin,end+1):
        res = scan.scan(target,str(i))
        res = res['scan'][target]['tcp'][i]['state']
        print(f'port {i} is {res}.')
        yop = (f'port {i} is {res}.')
        fic.write(yop)
        fic.write('\n')

    print()
    fic.close()
#-----------------------------------------------------------
def Imagen_download():
    print ("Descargando Imagenes de tu Universidad....................................")
    url = 'https://www.uanl.mx/'
    response = requests.get(url)
    parsed_body = html.fromstring(response.text)
    images = parsed_body.xpath('//img/@src')
    imagenes = [x for x in images if x.endswith('.jpg')]
    print(imagenes)
    os.system("mkdir images")
    for image in images:
        if image.startswith("http") == False:
            download = url + image
        else:
            download = image
            print(download)
            r = requests.get(download)
            f = open('images/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()

#------------------------------------------------------------------
def scraping_texto():
    print("Sacando la Informacion de tu Universidad:................................")
    html = urlopen("https://www.uanl.mx/")
    bs = BeautifulSoup(html.read(), features='lxml')
    rata = bs.html
    raton = bs.html.body.h1
    jack = rata.text
    jacks = raton.text
    rifa = open('scrapin.txt', 'w')
    rifa.write(jack)
    rifa.write('\n')
    rifa.write(jacks)
    rifa.write('\n')
    rifa.close()

#------------------------------------------------------------
def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        Nsec = exif['GPSInfo'][2][2] 
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][3] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}
         
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
            
def printMeta(r):
    ruta = r
    os.chdir(ruta)
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
            print ("Extrallendo informacion:...................")
            print ("[+++++] Metadata for file: %s " %(name))
            try:
                exifData = {}
                exif = get_exif_metadata(name)
                mama = open('meta.txt', 'w')
                for metadata in exif:
                    ratas = "Metadata: %s - Value: %s " %(metadata, exif[metadata])
                    mama.write(ratas)
                    mama.write('\n')
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
    

#-------------------------------------------------------------------------------
def hash_dehash():
    print ("Guardando Informacion:..............................")
    dicc1 = {}
    dicc2 = {}
    dicc3 = {}
    dicc4 = {}
    f = open(r'C:\Users\Manuel Lopez\Desktop\pia\images\meta.txt' , 'r' , errors='ignore').readlines()
    pio = open(r'C:\Users\Manuel Lopez\Desktop\pia\puertos.txt' , 'r' , errors='ignore').readlines()
    lin = open(r'C:\Users\Manuel Lopez\Desktop\pia\scrapin.txt' , 'r' , errors='ignore').readlines()
    war = open(r'C:\Users\Manuel Lopez\Desktop\pia\API_shodan.txt' , 'r' , errors='ignore').readlines()

    g = open("clavesHASH-meta.txt", 'w')
    gum = open("clavesHASH-puertos.txt", 'w')
    ball = open("clavesHASH-scraping.txt", 'w')
    dado = open("API_shodan_hash.txt", 'w')
    
    f = list(map(str.strip, f))
    pio = list(map(str.strip, pio))
    lin = list(map(str.strip, lin))
    war = list(map(str.strip, war))
    for i in f :
        enco = i
        h = hashlib.sha512(enco.encode())
        marte = h.hexdigest()
        g.write(marte)
        g.write("\n")
        dicc1[i] = marte 
        print(marte)
    g.close()
    for i in pio :
        enco = i
        h = hashlib.sha512(enco.encode())
        mierc = h.hexdigest()
        gum.write(mierc)
        gum.write("\n")
        dicc2[i] = mierc 
        print(mierc)
    gum.close()
    for i in lin :
        enco = i
        h = hashlib.sha512(enco.encode())
        juevc = h.hexdigest()
        ball.write(juevc)
        ball.write("\n")
        dicc3[i] = juevc 
        print(juevc)
    ball.close()
    for i in war :
        enco = i
        h = hashlib.sha512(enco.encode())
        vier = h.hexdigest()
        dado.write(vier)
        dado.write("\n")
        dicc4[i] = vier 
        print(vier)
    dado.close()

    print(dicc1)
    print(dicc2)
    print(dicc3)
    print(dicc4)

    clave = dicc1.keys()
    has = dicc1.values()
    elemento = dicc1.items()
    glave = dicc2.keys()
    haste = dicc2.values()
    element = dicc2.items()
    grave = dicc3.keys()
    gaste = dicc3.values()
    elementor = dicc3.items()
    madre = dicc4.keys()
    tarde = dicc4.values()
    elemental = dicc4.items()
    fic1 = open('meta_hash_512.txt', 'w')
    for clave, has in elemento :
        print(clave , '-', has)
        fic1.write(clave)
        fic1.write('--->')
        fic1.write(has)
        fic1.write('\n')
    fic1.close()
    fic2 = open('puert_hash_512.txt', 'w')
    for glave, haste in element :
        print(glave , '-', haste)
        fic2.write(glave)
        fic2.write('--->')
        fic2.write(haste)
        fic2.write('\n')
    fic2.close()
    fic3 = open('scrp_hash_512.txt', 'w')
    for grave, gaste in elementor :
        print(grave , '-', gaste)
        fic3.write(grave)
        fic3.write('--->')
        fic3.write(gaste)
        fic3.write('\n')
    fic3.close()
    fic4 = open('API_shodan_hash_512.txt', 'w')
    for madre, tarde in elemental :
        print(madre , '-', tarde)
        fic4.write(madre)
        fic4.write('--->')
        fic4.write(tarde)
        fic4.write('\n')
    fic4.close()

#------------------------------------------------------------------------------------
def correo_electronico():
    remitente = '111000Aninimus010201@gmail.com'
    destinatarios = ['christopherperrito@gmail.com']
    asunto = '[RPI] Correo de prueba'
    cuerpo = 'Este es el contenido del mensaje'
    ruta_adjunto = 'Reporte_general.txt'
    nombre_adjunto = 'Reporte_general.txt'

    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
     
    mensaje.attach(MIMEText(cuerpo, 'plain_uwu'))
    archivo_adjunto = open(ruta_adjunto, 'rb')
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    adjunto_MIME.set_payload((archivo_adjunto).read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    mensaje.attach(adjunto_MIME)
     
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login('111000Aninimus010201@gmail.com','UbuntuesloMaximo')
    texto = mensaje.as_string()
    sesion_smtp.sendmail(remitente, destinatarios, texto)
    sesion_smtp.quit()
#----------------------------------------------------------------------

if __name__ == "__main__":
    localIP = "192.168.1.91"
    localPort = 49669
    bufferSize = 2000
    UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    print("Servidor listo para enviar respuesta")
    escaneo_puertos()
    Imagen_download()
    scraping_texto()
    printMeta(r'C:\Users\Manuel Lopez\Desktop\pia\images')
    hash_dehash()
    todos_juntos()
    correo_electronico()

    while(True):
        recibido = UDPServerSocket.recvfrom(bufferSize)
        mensaje = recibido[0]
        ip = recibido[1]
        fi = str(recibido[1])
        respuesta = "Tu informacion se envio a tu correo"
        UDPServerSocket.sendto(str.encode(respuesta), ip)
        exit()

