import ast
import codecs
from typing import Union

import firebase_admin
from decouple import config
from firebase_admin import credentials, firestore

type = str(config("FIREBASE_CONNECTION_TYPE"))
project_id = str(config("FIREBASE_CONNECTION_PROJECT_ID"))
private_key_id = str(config("FIREBASE_CONNECTION_PRIVATE_KEY_ID"))
client_email = str(config("FIREBASE_CONNECTION_CLIENT_EMAIL"))
client_id = str(config("FIREBASE_CONNECTION_CLIENT_ID"))
auth_uri = str(config("FIREBASE_CONNECTION_AUTH_URI"))
token_uri = str(config("FIREBASE_CONNECTION_TOKEN_URI"))
auth_provider_x509_cert_url = str(config("FIREBASE_CONNECTION_AUTH_PROVIDER"))
client_x509_cert_url = config("FIREBASE_CONNECTION_CERT_URL")
universe_domain = str(config("FIREBASE_CONNECTION_UNIVERSE_DOMAIN"))
private_key = codecs.decode(config("FIREBASE_CONNECTION_PRIVATE_KEY"), "unicode_escape")

firebase_connection = {
    "type": type,
    "project_id": project_id,
    "private_key_id": private_key_id,
    "private_key": private_key,
    "client_email": client_email,
    "client_id": client_id,
    "auth_uri": auth_uri,
    "token_uri": token_uri,
    "auth_provider_x509_cert_url": auth_provider_x509_cert_url,
    "client_x509_cert_url": client_x509_cert_url,
    "universe_domain": universe_domain,
}

cred = credentials.Certificate(firebase_connection)
firebase_admin.initialize_app(cred)


# Create a new document in Firestore
def create_firebase_document(collection: str, document_data: object) -> str:
    db = firestore.client()
    doc_ref = db.collection(collection).document()
    doc_ref.set(document_data)
    return doc_ref.id


# Read a document from Firestore
def read_firebase_document(collection: str, document_id: str) -> Union[object, bool]:
    db = firestore.client()
    doc_ref = db.collection(collection).document(document_id)
    document = doc_ref.get()
    if document.exists:
        print("Document data:", document.to_dict())
        return document.to_dict()
    else:
        print("No such document!")
        return False
