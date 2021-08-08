from flask_seeder import Seeder
from jobbing.DBModels import Media

class MediaSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        print("seeding media")
        default_media = [Media(id=1, media="", link="https://www.youtube.com/watch?v=JHQECOrH9Yc&list=PLWVaDfmVrx0w4ldiNQrN03x2jbpE87bhW", title="¡Haz un Zoom!", size=, duration="5:56", created=datetime.datetime(2020, 6, 24), media_type="Video", views=83, likes=13, owner_id=1, album_id=1),
                    Media(id=2, media="", link="https://www.youtube.com/watch?v=QZpEpkhuPPg&list=PLWVaDfmVrx0x3MJVOvJGKbDP149_XS-72&index=1", title="Tu primera cuenta de Gmail", size=, duration="5:47", created=datetime.datetime(2020, 6, 19), media_type="Video", views=63, likes=12, owner_id=1, album_id=2),
                    Media(id=3, media="", link="https://www.youtube.com/watch?v=S7xrjwEV0WM&list=PLWVaDfmVrx0w6sKB1X6Kj4BKIvU0RHcux", title="Así es como vendes", size=, duration="7:35", created=datetime.datetime(2020, 6, 12), media_type="Video", views=412, likes=21, owner_id=1, album_id=3),
                    Media(id=4, media="", link="https://www.youtube.com/watch?v=vBgPyPRTvv0&list=PLWVaDfmVrx0wOYC32Tijb4tZHiGcXvrVs", title="Tú eres tu propia marca", size=, duration="11:41", created=datetime.datetime(2020, 6, 17), media_type="Video", views=213, likes=25, owner_id=1, album_id=4),
                    Media(id=5, media="", link="https://www.youtube.com/watch?v=tQEw4P0oFYk&list=PLWVaDfmVrx0xQWPQEJYP2A9YjXyEglYVp", title="¡No hagas compras de pánico!", size=, duration="2:33", created=datetime.datetime(2020, 6, 10), media_type="Video", views=214, likes=17, owner_id=1, album_id=5),
                    Media(id=6, media="", link="https://www.youtube.com/watch?v=Z41JSIQIOC4&list=PLWVaDfmVrx0zIMAzz0aYYFlo1AL20ilAA", title="¡Evita la desinformación!", size=, duration="3:47", created=datetime.datetime(2020, 6, 5), media_type="Video", views=123, likes=15, owner_id=1, album_id=6)]

        for media in default_albums:
            self.db.session.add(media)