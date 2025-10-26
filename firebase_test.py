import firebase_admin
from firebase_admin import credentials, firestore

# 🔑 आपला Firebase key path द्या (तसाच जसा आहे)
cred = credentials.Certificate("firebase_config/serviceAccountKey.json")

# 🔥 Firebase App initialize
firebase_admin.initialize_app(cred)

# 🔍 Firestore client तयार करा
db = firestore.client()

# ✅ Test document लिहूया
test_ref = db.collection("test_collection").document("demo_doc")
test_ref.set({
    "message": "Firebase connected successfully!",
    "status": True
})

# 🔁 Read back
doc = test_ref.get()
print("📄 Document Data:", doc.to_dict())
