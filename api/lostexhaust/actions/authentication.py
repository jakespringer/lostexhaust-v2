import re, os, M2Crypto, base64, util
import lostexhaust.config as config

rsakey = M2Crypto.RSA.load_pub_key(os.path.join(config.get('rootDir'), config.get("catlinRsaPemFile")))

def check_token_validity(token, ip, timestamp):
    parsed = parse_token(decrypt_rsa(token))
    if parsed is None:
        return False
    else:
        (parsed_person_id, parsed_timestamp, parsed_ip) = parsed
        # todo: check if person_id is valid
        valid_person_id = True
        valid_ip = parsed_ip == ip or ip == "127.0.0.1"
        valid_timestamp = (timestamp - int(parsed_timestamp)) < config.get("loginSessionDuration")
        return valid_person_id and valid_ip and valid_timestamp

def decrypt_rsa(encoded):
    try:
        cipher = base64.b16decode(encoded)
        plain = rsakey.public_decrypt(cipher, M2Crypto.RSA.pkcs1_padding)
        return plain
    except:
        return ""

def parse_token(unencrypted_token):
    tokens = unencrypted_token.split("|")
    if (len(tokens) != 3):
        return None
    else:
        return tuple(tokens)

def get_person_from_token(token):
    parsed = parse_token(decrypt_rsa(token))
    if parsed is None:
        return None
    else:
        (parsed_person_id, parsed_timestamp, parsed_ip) = parsed
        return parsed_person_id
