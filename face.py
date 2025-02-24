import cv2

# Load model Haar Cascade untuk deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fungsi untuk mendeteksi wajah dari gambar
def detect_faces(image):
    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Gambar kotak di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return image

# Menggunakan webcam untuk deteksi wajah secara real-time
def detect_faces_from_webcam():
    # Buka webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Baca frame dari webcam
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Deteksi wajah pada frame
        frame_with_faces = detect_faces(frame)
        
        # Tampilkan frame dengan wajah yang terdeteksi
        cv2.imshow('Face Detection', frame_with_faces)
        
        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
    
    # Tutup webcam dan jendela
    cap.release()
    cv2.destroyAllWindows()

# Menggunakan gambar untuk deteksi wajah
def detect_faces_from_image(image_path):
    # Baca gambar
    image = cv2.imread(image_path)
    
    if image is None:
        print("Gambar tidak ditemukan atau tidak bisa dibuka.")
        return
    
    # Deteksi wajah pada gambar
    image_with_faces = detect_faces(image)
    
    # Tampilkan gambar dengan wajah yang terdeteksi
    cv2.imshow('Face Detection', image_with_faces)
    
    # Tunggu hingga pengguna menekan tombol apa pun
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Pilih mode deteksi (webcam atau gambar)
if __name__ == "__main__":
    mode = input("Pilih mode deteksi (webcam/image): ").strip().lower()
    
    if mode == "webcam":
        detect_faces_from_webcam()
    elif mode == "image":
        image_path = input("Masukkan path gambar: ").strip()
        detect_faces_from_image(image_path)
    else:
        print("Mode tidak valid. Pilih 'webcam' atau 'image'.")