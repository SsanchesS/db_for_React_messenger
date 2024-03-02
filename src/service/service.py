import os
import base64
import uuid   # Можно с uuid5
import imghdr # для определения типа файла

def decode_and_write(avatar_file,old_avatar_file_path=None):
    try:
        if old_avatar_file_path is not None:
            if not old_avatar_file_path == 'user_files/default_avatar_file.png':
                os.remove(old_avatar_file_path)
            
        image_type, avatar_file = avatar_file.split(',')  # Можно просто извлечь из image_type

        decoded_data = base64.b64decode(avatar_file)

        file_name = str(uuid.uuid4())[:12]
        image_type = imghdr.what(None, h=decoded_data)
        if not image_type:
            raise ValueError("Невозможно определить расширение файла")
        
        file_path = f"user_files/usersFiles/{file_name}.{image_type}" ################## путь
        with open(file_path, 'wb') as file:        
            file.write(decoded_data)
        return file_path

    except Exception as e:
        print(f"Ошибка {e}")
        return None
    
def get_and_encode(file_path):
    try:
        with open(file_path, 'rb') as file:        
            data = file.read()
        image_type = imghdr.what(None, h=data)
        encoded_data = base64.b64encode(data).decode('utf-8') # байты в строку        
        if not image_type:
            raise ValueError("Невозможно определить расширение файла")
        avatar_file = f"data:image/{image_type};base64,{encoded_data}"
        return avatar_file

    except Exception as e:
        print(f"Ошибка {e}")
        return None