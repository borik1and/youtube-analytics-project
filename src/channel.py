import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.channel_title = None
        self.channel_description = None
        self.url = None
        self.num_subscribers = None
        self.video_count = None
        self.total_views = None
        self.__api_key = os.getenv('YT_API_KEY')
        self.get_channel_info()

        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""

    @classmethod
    def get_service(cls):
        __api_key = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=__api_key)
        return youtube

    def get_channel_info(self):
        youtube = self.get_service()
        channel_data = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        if 'items' in channel_data:
            channel_data = channel_data['items'][0]
            self.channel_title = channel_data['snippet']['title']
            self.channel_description = channel_data['snippet']['description']
            self.url = f"https://www.youtube.com/channel/{self.channel_id}"
            self.num_subscribers = int(channel_data['statistics']['subscriberCount'])
            self.video_count = int(channel_data['statistics']['videoCount'])
            self.total_views = int(channel_data['statistics']['viewCount'])


    def to_json(self, filename):
        channel_data = {
            'channel_id': self.channel_id,
            'channel_title': self.channel_title,  # Corrected key name
            'channel_description': self.channel_description,
            'channel_link': self.url,
            'num_subscribers': self.num_subscribers,
            'num_videos': self.video_count,
            'total_views': self.total_views
        }
        with open(filename, 'w') as file:
            json.dump(channel_data, file)

    def print_info(self) -> None:
        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('YT_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        playlists = youtube.playlists().list(channelId=self.channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        """Выводит в консоль информацию о канале."""

        print(playlists)
