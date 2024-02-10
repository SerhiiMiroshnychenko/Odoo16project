import json

from odoo import http
from odoo.http import request, route

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleController(WebsiteSale):

    # @http.route([
    #     '/shop',
    #     '/shop/page/<int:page>',
    #     '/shop/category/<model("product.public.category"):category>',
    #     '/shop/category/<model("product.public.category"):category>/page/<int:page>',
    # ], type='http', auth="public", website=True, sitemap=sitemap_shop)
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        print('============ my shop page =============')
        return super().shop(page, category, search, min_price, max_price, ppg, **post)

    @route('/my_shop', website=True, type='http')
    def my_shop(self):
        print('============ MY SHOP PAGE =============')
        return self.shop()
