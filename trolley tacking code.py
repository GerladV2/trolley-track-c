import pyrebase
import time

# Firebase Configuration
firebaseConfig = {
    "apiKey":  "AIzaSyAvUrig_e2AivOwAGa3Yfgi3ueW3h9Xa10",
    "authDomain": "fir-realtimedata-9fab9.firebaseapp.com",
    "databaseURL": "https://fir-realtimedata-9fab9-default-rtdb.firebaseio.com",
    "projectId": "fir-realtimedata-9fab9",
    "storageBucket": "fir-realtimedata-9fab9.firebasestorage.app",
    "messagingSenderId": "856493742927",
    "appId": "1:856493742927:web:f0655d57a7804257bc833a"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

def fetch_gps_data():
    """Fetch the latest GPS coordinates from Firebase."""
    data = db.get().val()  # Get the entire database dictionary
    if data and "LAT" in data and "LNG" in data:
        return float(data["LAT"]), float(data["LNG"])
    return None, None

# Loop to continuously update coordinates
while True:
    try:
        lat, lng = fetch_gps_data()
        if lat is not None and lng is not None:
            print(f"Updated Location: Latitude={lat}, Longitude={lng}")
        else:
            print("Waiting for GPS data from Firebase...")

        time.sleep(5)  # Refresh every 5 seconds

    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")
        break
    except Exception as e:
        print(f"Error fetching GPS data: {e}")
