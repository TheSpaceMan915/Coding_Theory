from encoding import *
from decoding import *

def menu():
    while(True):
        print("What would you like to do?")
        print("1) Encode MyMy")
        print("2) Decode MyMy")
        print("3) Encode a picture")
        print("4) Decode a picture")
        value = input()

        match value:
            case "1":
                dictSize = 400
                bufferSize = 200
                text_bits = b_encode("../files/MyMy.txt")
                text_utf = text_bits.decode("UTF-8")

                print("Bits: ", text_utf)

                with open("../files/message_encoded.json", 'w') as f:
                    encodeLZSS(dictSize, bufferSize, text_utf)
                    mess_enc_fano = encodeFano(text_utf)
                    json.dump(mess_enc_fano, f)

            case "2":
                dictSize = 400
                file_name = "../files/message_encoded.json"
                dec = decodeFano(file_name)
                decodeLZSS(dictSize, dec)

                b = decode_76(dec.encode("UTF-8"))
                with open("../files/text_decoded.txt", "wb") as f:
                    f.write(b)

            case "3":
                dictSize = 280
                bufferSize = 100
                picture_bits = b_encode("../files/pic.bmp")
                picture_utf = picture_bits.decode("UTF-8")

                with open("../files/message_encoded.json", 'w') as f:
                    encodeLZSS(dictSize, bufferSize, picture_utf)
                    mess_enc_fano = encodeFano(picture_utf)
                    json.dump(mess_enc_fano, f)

            case "4":
                dictSize = 280
                file_name = "../files/message_encoded.json"
                dec = decodeFano(file_name)
                decodeLZSS(dictSize, dec)

                b = decode_76(dec.encode("UTF-8"))
                imag = Image.open(io.BytesIO(b))
                imag.save("../files/image_decoded.bmp")

            case _:
                sys.exit(10)


if __name__ == "__main__":
    menu()