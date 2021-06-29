import requests


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self, token, file_name=''):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        if file_name == '':
            file_name = self.file_path.split('/')[-1]
        params = {"path": file_name, "overwrite": "true"}
        href = requests.get(url=url, headers=headers, params=params)
        response = requests.put(href.json()['href'], data=open(self.file_path, 'rb'))
        if response.status_code == 201:
            return 'Success'


if __name__ == '__main__':
    token = ''
    uploader = YaUploader('C://Users//marin//Desktop//Pics//Screen//x_d0a65337.jpg')
    result = uploader.upload(token)
    print(result)
