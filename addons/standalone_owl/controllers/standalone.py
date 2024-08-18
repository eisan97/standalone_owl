from odoo.http import request, route, Controller

class StandaloneController(Controller):
    @route("/standalone_owl", auth="public")
    def standalone_app(self):
        return request.render(
            'standalone_owl.standalone_app',
            {
                'session_info':request.env['ir.http'].get_frontend_session_info(),
            }
        )