# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 23:00:17 2018

@author: machao
"""
import os
model_dir =os.getcwd()
print(model_dir)
import sys
sys.path.append(model_dir)
import spider

w, l, h, z, t, dytt, s, douban = spider.import_()

catalog_wow = w.wow_lists()
catalog_lol = l.lol_lists()
catalog_hs = h.hs_lists()
catalog_lt = t.longteng_lists()
catalog_sky = s.get_gamesky()

catalog_dy1 = dytt.dy2018_movie()
catalog_dy2 = dytt.dytt8_movie()

print(catalog_dy1)
