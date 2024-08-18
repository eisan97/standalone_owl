{
    'name':'Standalone OWL',
    'author':'Thin Ei San',
    'depends':['base','web'],
    'data':[
        'views/view.xml',
        'views/menu.xml',
    ],
    'license':'LGPL-3',
    'assets': {
        'standalone_owl.assets_standalone_app': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'standalone_owl/static/src/**/*',
        ],
    },

}