from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
app = firebase_admin.initialize_app(cred)


# Crea un nuevo documento en Firestore
db = firestore.client()

class City:
    def __init__(self, name, state, country, capital=False, population=0, regions=[]):
        self.name = name
        self.state = state
        self.country = country
        self.capital = capital
        self.population = population
        self.regions = regions

    @staticmethod
    def from_dict(source):

        pass
    def to_dict(self):
      
        pass
    def __repr__(self):
        return f"City(\
                name={self.name}, \
                country={self.country}, \
                population={self.population}, \
                capital={self.capital}, \
                regions={self.regions}\
            )"




cities_ref = db.collection("cities")
cities_ref.document("BJ").set(
    City("Beijing", None, "China", True, 21500000, ["hebei"]).to_dict()
)
cities_ref.document("SF").set(
    City(
        "San Francisco", "CA", "USA", False, 860000, ["west_coast", "norcal"]
    ).to_dict()
)
cities_ref.document("LA").set(
    City(
        "Los Angeles", "CA", "USA", False, 3900000, ["west_coast", "socal"]
    ).to_dict()
)
cities_ref.document("DC").set(
    City("Washington D.C.", None, "USA", True, 680000, ["east_coast"]).to_dict()
)
cities_ref.document("TOK").set(
    City("Tokyo", None, "Japan", True, 9000000, ["kanto", "honshu"]).to_dict()
)

doc_ref = db.collection("cities").document("SF")

doc = doc_ref.get()

if doc.exists:
    print(f"Document data: {doc.to_dict()}")
else:
    print("No such document!")


docs = db.collection("cities").stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")