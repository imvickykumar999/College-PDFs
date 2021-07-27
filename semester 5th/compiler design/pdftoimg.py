from pdf2image import convert_from_path
import easygui
pdf = easygui.fileopenbox()
# Store Pdf with convert_from_path function
images = convert_from_path(pdf)
m=0
for img in images:
    m+=1
    img.save("img"+str(m)+'.jpg', 'JPEG')
