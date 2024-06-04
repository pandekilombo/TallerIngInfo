
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from google.cloud.firestore_v1.base_query import FieldFilter


# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
app = firebase_admin.initialize_app(cred)


# Crea un nuevo documento en Firestore
db = firestore.client()
doc_ref = db.collection("Usuario").document("Admin")
doc_ref.set({"Nombre": "Miguel","Apellido": "Contreras", "Contraseña": "1234", "Rol": "Admin"})
# se imprime rol nombre contraseña apellido

##GET SIMPLE
print("PRIMER GET")
doc = doc_ref.get()
if doc.exists:
    print(f"Document data: {doc.to_dict()}")
else:
    print("No such document!")

print("\n\n")



#GET CON FILTRO 
print("SEGUNDO GET")
docs = (
    db.collection("Usuario")
    .where(filter=FieldFilter("Nombre", "==", "Miguel"))
    .stream()
)

for doc in docs:
    nombre = doc.to_dict().get("Nombre")  # Obtén el valor de la casilla "Nombre"
    print(f"Nombre del doc: {nombre}")


print("\n")


#GET GENERAL - IMPRIME TODOO
print("TERCER GET")
docs = db.collection("Usuario").stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")



#Get solo el nombre

print("\n\nCUARTO GET")

docs = (
    db.collection("Usuario")
    .where(filter=FieldFilter("Nombre", "==", "Miguel"))
    .stream()
)

for doc in docs:
    nombre = doc.to_dict().get("Nombre")  # Obtén el valor de la casilla "Nombre"
    print(f"Nombre del doc: {nombre}")


print("\nQuinto get")


# Supongamos que tienes una referencia al documento
doc_ref = db.collection("Usuarios").document("Miguel_Contreras1")

# Obtén el ID del documento
document_id = doc_ref.id

print(f"ID del documento: {document_id}")



docs = (
    db.collection("Usuario")
    .where(filter=FieldFilter("Nombre", "==", "Miguel"))
    .stream()
)

for doc in docs:
    nombre = doc.to_dict().get("Nombre")  # Obtén el valor de la casilla "Nombre"
    user_id = doc.id
    print(f"Nombre del doc: {nombre}")
    print(f"ID:{user_id}")
    

print("CHECK USER FUNCIONANDO \n\n")
def Check_User(Usuario):
    #  doc_ref = db.collection("Usuario")
    doc_ref = db.collection("Usuarios").document(Usuario)
    DocCheck = doc_ref.get()
    if DocCheck.exists:
        nombre = DocCheck.to_dict().get("Nombre")
        print(f"Nombre del doc: {nombre}")
        return True
    else:
        print("El documento no existe o no se encontró.")
        return False
    

print(Check_User("Miguel_Contreras1"))