import re
import lostexhaust.config
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

pem = ""
with open(config.get("catlinRsaPemFile"), "r") as pem_file:
    pem = pem_file.read()

def check_token_validity(token, ip, timestamp):
    # temporary
    return True

    (parsed_person_id, parsed_ip, parsed_timestamp) = parse_token(decrypt_rsa(token, pem))
    # todo: check if person_id is valid
    valid_person_id = True
    valid_ip = parsed_ip == ip
    valid_timestamp = (timestamp - int(parsed_timestamp)) < config.get("loginSessionDuration")
    return valid_person_id and valid_ip and valid_timestamp

def decrypt_rsa(encrypted, key):
    rsakey = RSA.importKey(key)
    dcipher = PKCS1_v1_5.new(rsakey)
    return dcipher.decrypt(encrypted)

def parse_token(unencrypted_token):
    tokens = unencrypted_token.split("|")
    if (len(tokens) != 3):
        return None
    else:
        return tuple(tokens)

def get_person_from_token(token):
    (parsed_person_id, parsed_ip, parsed_timestamp) = parse_token(decrypt_rsa(token, pem))
    return parsed_person_id
