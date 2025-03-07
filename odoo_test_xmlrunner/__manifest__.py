{
    "name": "Unittest xUnit reports",
    "version": "16.0.1.0.1",
    "depends": ["base"],
    "author": "Smile, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "summary": """
    This module override Odoo testing method to run them with xmlrunner tool.
    """,
    "website": "https://github.com/OCA/server-tools",
    "category": "Tools",
    "sequence": 20,
    "installable": True,
    "application": False,
    "external_dependencies": {
        "python": ["unittest-xml-reporting"],
    },
}
