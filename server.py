import pyqrcode
import png
import rsa
from pyqrcode import QRCode

def generate_qr(s, filename):
  url = pyqrcode.create(s)

  url.svg(filename, scale=8)

def vigenere_enc(plainteks, key):
  plainteks = plainteks.upper()
  key = key.upper()

  _cipher = list()
  index = 0
  for i in plainteks:
    _index = index % 3

    k = ord(key[_index])
    temp = (ord(i) + k)

    if temp > 90:
      temp = temp - 65

    _cipher.append(temp)
    index = index + 1

  cipher = ''
  for c in _cipher:
    cipher = cipher + chr(c)

  return cipher


def rsa_enc(plainteks, key):
  (riska_pub, riska_priv) = rsa.newkeys(key)

  message = plainteks.encode('utf8')

  crypto = rsa.encrypt(message, riska_pub)

  return (crypto.hex(), riska_priv)


plainteks = "plainteks"
generate_qr(plainteks, 'myqr-plain.png')
key = "abc"

e = vigenere_enc(plainteks, key)
generate_qr(e, 'myqr-vigen.png')

(e, private_key) = rsa_enc(e, 512)

print(e)

generate_qr(e, 'myqr-rsa.png')
