import qrcode
import shutil
import os

def QRcode():

    details = input('Enter text: ')
    i = input('save as: ')

    img = qrcode.make(details)
    filename = f'createqrcode {i}.png'
    img.save(filename)

    first_location = os.path.abspath(filename)  # get full path of the created file
    changed_location = os.path.join('C:/Users/Ramiru/Documents/Python/QR/QR codes generated', filename)

    shutil.move(first_location, changed_location)
    print('Filed saved to local storage successfully')

    again = input('Do you want to create another qrcode (yes/no): ').title()

    if again == 'Yes':
        QRcode() 
    elif again == 'No':
        print('Thank you for creating with us. Please visit your local storage')

QRcode()



















