# -*- coding: utf-8 -*-
import sys
sys.path.append(r'D:\学习\技巧\package')
import class_wow as wow
import class_lol as lol
import class_zhihu as zh
import class_HS as hs
import class_longteng as lt
import class_dytt as dy
import class_gamesky as sky
import class_douban as db
import class_tieba as tieba_


def import_():
    w = wow.WoW()
    l = lol.LoL()
    h = hs.HS()
    z = zh.Zhihu()
    t = lt.LongTeng()
    dytt = dy.Dytt()
    s = sky.Gamesky()
    douban = db.Douban()
    tb = tieba_.TieBa()
    return w, l, h, z, t, dytt, s, douban, tb





