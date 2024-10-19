from pymongo import MongoClient

# เชื่อมต่อกับ MongoDB ที่รันในเครื่อง (หรือใช้ connection string ถ้าใช้ MongoDB Atlas)
client = MongoClient('mongodb://localhost:27017/')

# สร้างหรือเลือกฐานข้อมูล (database)
db = client['mydatabase']

# สร้างหรือเลือกคอลเล็กชัน (คล้ายกับตารางในฐานข้อมูล SQL)
collection = db['mycollection']

# ฟังก์ชันสำหรับเพิ่มเอกสารใหม่
def create_document():
    new_document = {
        "name": "Router HQ",
        "device_info": {
            "device_type": "cisco_ios",
            "ip": "192.168.1.1",
            "username": "admin",
            "password": "admin",
            "secret": "secret"
        }
    }
    # เพิ่มเอกสารลงในคอลเล็กชัน
    result = collection.insert_one(new_document)
    print(f'Document inserted with ID: {result.inserted_id}')


# ฟังก์ชันสำหรับดึงเอกสารทั้งหมด
def read_documents():
    documents = collection.find()  # ดึงข้อมูลทั้งหมด
    for doc in documents:
        print(doc)

# ฟังก์ชันสำหรับดึงข้อมูลตามเงื่อนไข (เช่น ดึงเฉพาะเอกสารที่มี name = 'Router HQ')
def read_document_by_name(name):
    document = collection.find_one({"name": name})
    if document:
        print(document)
    else:
        print("No document found")

# ฟังก์ชันสำหรับอัปเดตเอกสารตามเงื่อนไข (เช่น อัปเดต IP ของอุปกรณ์)
def update_document(name, new_ip):
    result = collection.update_one(
        {"name": name},  # เงื่อนไขการค้นหา
        {"$set": {"device_info.ip": new_ip}}  # ค่าใหม่ที่ต้องการอัปเดต
    )
    if result.modified_count > 0:
        print(f"Document updated successfully")
    else:
        print("No document matched the query")

# ฟังก์ชันสำหรับลบเอกสารตามเงื่อนไข
def delete_document(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Document deleted successfully")
    else:
        print("No document matched the query")

if __name__ == "__main__":
    # เพิ่มเอกสารใหม่
    create_document()

    # อ่านข้อมูลทั้งหมด
    print("Documents in collection:")
    read_documents()

    # อัปเดตข้อมูล
    print("\nUpdating document...")
    update_document("Router HQ", "10.0.0.2")

    # อ่านข้อมูลที่ถูกอัปเดต
    print("\nDocuments after update:")
    read_documents()

    # ลบข้อมูล
    # print("\nDeleting document...")
    # delete_document("Router HQ")

    # อ่านข้อมูลทั้งหมดอีกครั้ง
    print("\nDocuments after deletion:")
    read_documents()
