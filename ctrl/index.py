#coding:utf-8

from _handler import Handler
from _urlmap import urlmap
from model.url_short import url_short_new
 
@urlmap('/')
class Index(Handler):
    def get(self):
        url = self.get_argument('url', '')

        host = self.request.host
        url_short = "%s/%s"%(
            host,
            url_short_new(url)
        )

        self.render(
            url=url,
            url_short=url_short
        )

