import hashlib
import base64

def banner():
    return r"""
        ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
        ██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
        ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║       ██║   ██║   ██║██║   ██║██║     
        ██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║       ██║   ██║   ██║██║   ██║██║     
        ╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
        ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                        This script is designed to help you with cryptography tasks.
                                    Welcome to the Advanced Hashing Utility!
                                          Auther : Arbab Gul
                                            Version : 3.0"""

class CrptographyUtils:

    # Encryption methods
    @staticmethod
    def md5(text):
        return hashlib.md5(text.encode('utf-8')).hexdigest()

    @staticmethod
    def sha1(text):
        return hashlib.sha1(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def sha256(text):
        return hashlib.sha256(text.encode('utf-8')).hexdigest()

    @staticmethod
    def sha512(text):
        return hashlib.sha512(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def sha3_256(text):
        return hashlib.sha3_256(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def sha3_512(text):
        return hashlib.sha3_512(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def blake2s(text):
        return hashlib.blake2s(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def blake2b(text):
        return hashlib.blake2b(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def base64_encode(text):
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')

    @staticmethod
    def bytes_to_hexdigest(byte_string):
        return byte_string.hex()

    # Decryption methods
    # ----------------------------
    @staticmethod
    def md5_decrypt(hash_value):
        pass

def main():
    print(banner())

    try:
        choose = int(input("Choose an option:\n1.MD5 \n2.SHA1 \n3.SHA256 \n4.SHA-512 \n5.SHA3-256 \n6.SHA3-512 \n7.BLAKE2s \n8.BLAKE2b \n9.BASE64 \n10.HEX \n11.Exit \nSelect Encryption method: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 11.")
        return


    text = input("Enter the text: ")
    match choose:
        case 1:
            print(f"MD5 Hash: {CrptographyUtils.md5(text)}")
        case 2:
            print(f"SHA1 Hash: {CrptographyUtils.sha1(text)}")
        case 3:
            print(f"SHA256 Hash: {CrptographyUtils.sha256(text)}")
        case 4:
            print(f"SHA512 Hash: {CrptographyUtils.sha512(text)}")
        case 5:
            print(f"SHA3-256 Hash: {CrptographyUtils.sha3_256(text)}")
        case 6:
            print(f"SHA3-512 Hash: {CrptographyUtils.sha3_512(text)}")
        case 7:
            print(f"BLAKE2s Hash: {CrptographyUtils.blake2s(text)}")
        case 8:
            print(f"BLAKE2b Hash: {CrptographyUtils.blake2b(text)}")
        case 9:
            print(f"Base64 Encoded: {CrptographyUtils.base64_encode(text)}")
        case 10:
            print(f"Hex Digest: {CrptographyUtils.bytes_to_hexdigest(text.encode('utf-8'))}")
        case 11:
            print("Exiting the program.")
            exit(1)
        case _:
            print("Invalid choice. Please select a number between 1 and 11.")
            return
main()