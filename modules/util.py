import os
import hmac
import hashlib
from flask import request

SECRET = os.environ.get("SECRET")


def validate_signature():
    key = bytes(SECRET, 'utf-8')
    expected_signature = hmac.new(
        key=key, msg=request.data, digestmod=hashlib.sha256).hexdigest()
    incoming_signature = request.headers.get(
        'X-Hub-Signature-256').split('sha256=')[-1].strip()
    return hmac.compare_digest(incoming_signature, expected_signature)
