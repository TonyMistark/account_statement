# coding=utf-8

import xadmin
from xadmin.views.dashboard import AppDashboard


class CouponIndex(AppDashboard):
    app_label = 'coupon'
    template = 'coupon/app_dashboard.html'
    widget_customiz = False

xadmin.site.register_appindex(CouponIndex)

import admins
