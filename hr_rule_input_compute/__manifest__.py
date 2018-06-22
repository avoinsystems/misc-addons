{
    "name": """Compute Salary Inputs""",
    "summary": """Allows to compute amounts of inputs in salary rules""",
    "category": "Human Resources",
    # "live_test_URL": "",
    "images": ["static/description/icon.png"],
    "version": "1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev",
    "support": "apps@it-projects.info",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    # "price": 9.00,
    # "currency": "EUR",

    "depends": [
        'hr_payroll',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'security/hr_rule_input_compute_security.xml',
        'views/hr_payroll_views.xml',
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": False,
}