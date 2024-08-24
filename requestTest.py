import requests

def fromLocal():
    url = 'http://127.0.0.1:5000/process_image'
    files = {'file': open('E:\\Dataset Multispectral\\Dataset_Mapir\\NormalRGN_Unpad\\2024_0613\\A1.JPG', 'rb')}
    
    try:
        resp = requests.post(url, files=files)
        
        # Cetak respons teks untuk debugging
        print('Response Text:', resp.text)
        
        # Coba parsing JSON, atau tangani kesalahan jika terjadi
        try:
            json_resp = resp.json()
            print(json_resp)
        except requests.exceptions.JSONDecodeError:
            print('Error decoding JSON. Response content is not in JSON format.')
            print(resp.text)
    
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")

if __name__ == '__main__':
    fromLocal()
