# -*- coding: utf-8 -*-
import sys
sys.path.append(r'D:\学习\技巧\package')
import spider

w, l, h, z, t, dytt, s, douban, tb= spider.import_()

catalog_wow = w.wow_lists()
catalog_lol = l.lol_lists()
catalog_hs = h.hs_lists()
catalog_lt = t.longteng_lists()
catalog_sky = s.get_gamesky()

catalog_dy1 = dytt.dy2018_movie()
catalog_dy2 = dytt.dytt8_movie()
douban.info('')
douban.pinglun(1)

w.read_wow('', 1)
l.read_lol('', 1)
h.read_hs('', 1)
t.read_longteng('')

catalog_zhihu = z.zh_lists('')
z.read_zhihu('', 1)

list_tieba = tb.tieba('')
tb.read_tieba('',1)
