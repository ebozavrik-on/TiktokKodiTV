import xbmcgui
import requests

def get_tiktok_videos():
    # API-запрос к TikTok, чтобы получить список видеороликов
    api_url = 'https://api.tiktok.com/v1/videos'
    params = {'limit': 10, 'cursor': 0}
    response = requests.get(api_url, params=params)

    # Парсим JSON-ответ и извлекаем данные о видео
    videos = []
    for item in response.json()['items']:
        videos.append({
            'title': item['title'],
            'description': item['description'],
            'thumbnail': item['thumbnail']['url']
        })

    return videos

def main():
    videos = get_tiktok_videos()
    for video in videos:
        print(f"Заголовок: {video['title']}")
        print(f"Описание: {video['description']}")
        print(f"Тхумбнэйл: {video['thumbnail']}")

if __name__ == '__main__':
    main()