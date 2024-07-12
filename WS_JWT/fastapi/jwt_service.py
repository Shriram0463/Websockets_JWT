import jwt
import logging

SECRET_KEY = "secret_test"

def decode_jwt(token: str) -> str:
    #print(f"Using SECRET_KEY: {SECRET_KEY}")
    try:
        # Decode header and payload without verification
        #header = jwt.get_unverified_header(token)
        #payload = jwt.decode(token, options={"verify_signature": False})
        #print(f"Token Header: {header}")
        #print(f"Token Payload: {payload}")
        
        # Now try to decode with verification
        verified_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        logging.info(f"Successfully decoded payload: {verified_payload}")
        return verified_payload["sub"]
    except jwt.ExpiredSignatureError:
        logging.error("Token expired")
        return "Token expired"
    except jwt.InvalidTokenError as e:
        logging.error(f"Invalid token: {e}")
        return "Invalid token"