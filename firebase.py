from typing import Union

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
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
