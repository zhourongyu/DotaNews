#!/usr/bin/env python

from _db import _db


def url_short_new(url):
    id = _db.get( 'select `id` from url_short where url=%s limit 1', url)
    if id:
        id = id.id
    else:
        id = _db.execute( 'insert into `url_short` (url) values (%s)', url)
    return id

if __name__ == "__main__":
    print url_short_new("http://pma.tools.sinaapp.com/index.php?db=app_z007")
    from time import time
    print url_short_new("http://pma.tools.sinaapp.com/index.php?db=app_z007?%s"%time())

