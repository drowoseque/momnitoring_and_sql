from tornado.web import RequestHandler
from typing import List, Tuple

from mas.web.handlers import PingHandler, AddFavoriteHandler, GetFavoriteHandler

ping_url = (r'/ping/', PingHandler)

custom_urls = [
    (r'/add/', AddFavoriteHandler),
    (r'/get/', GetFavoriteHandler),
]


def get_all_urls() -> List[Tuple[str, RequestHandler]]:
    return custom_urls + [ping_url]
