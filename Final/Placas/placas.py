import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

placa = []

# Lectura de la imagen
image = cv2.imread('auto001.jpg')

# Conversión a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Proceso de suavizado de la imagen
gray = cv2.blur(gray,(3,3))

# Algoritmo de detección de bordes
canny = cv2.Canny(gray,150,200)

# Algoritmo para resaltar los bordes detectados
canny = cv2.dilate(canny,None,iterations=1)

# Algoritmo para unir de manera continua los contornos
# Encuentra todos los contornos presentes en la imagen
#_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# Función para dibujar todos los contornos encontrados
#cv2.drawContours(image,cnts,-1,(0,255,0),2)
for c in cnts:
    # Encuentra el área del contorno
    area = cv2.contourArea(c)
        
    # Calcula el rectángulo del contorno
    x,y,w,h = cv2.boundingRect(c)
    epsilon = 0.09*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)

    # Si tiene 4 vértices y un área aproximada de 9000, parece una placa
    if len(approx)==4 and area>9000:
        
        # Imprime el área
        print('area=',area)
        
        # Calcula la relación anchura-altura
        #cv2.drawContours(image,[approx],0,(0,255,0),3)
        aspect_ratio = float(w)/h
        
        # Si la relación es 2.4, el rectángulo es muy parecido a la placa
        if aspect_ratio>2.4:
        
            # En las siguientes instrucciones se imprimen los datos de la placa 
            # y se la muestra en una ventana
            placa = gray[y:y+h,x:x+w]
            
            # Se extrae el texto asociado a la placa utilizando Tesseract
            text = pytesseract.image_to_string(placa,config='--psm 11')

            # Se imprime la texto de la placa encontrada
            print('PLACA: ',text)

            # Se muestra una imagen de la placa
            cv2.imshow('PLACA',placa)

            # Se agrega un texto a la imagen, indicando los datos encontrados
            cv2.moveWindow('PLACA',780,10)
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(image,text,(x-20,y-10),1,2.2,(0,255,0),3)

# Se muestran los datos obtenidos
cv2.imshow('Image',image)
cv2.moveWindow('Image',45,10)
cv2.waitKey(0)