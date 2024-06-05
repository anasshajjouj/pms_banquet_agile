{
    'name': 'Product Pack',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': 'Manage Products as Pack',
    'description': """Selling products in a pack is a great way to raise average 
    sales price per product, to serve customers with products that make their 
    lives easier, and to leverage current products into new and different ones.
    They are profitable for smaller businesses as well as large ones.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['sale_management', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_views.xml',
        'views/res_partner_view.xml',
        'views/product_template_views.xml',
        'views/sale_order_views.xml',
        'views/personnel_views.xml',
        'views/job_category_views.xml',
    ],
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
