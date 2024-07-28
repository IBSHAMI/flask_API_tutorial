from flask.views import MethodView


class TestView(MethodView):
    """
    TestView class api view
    """

    def get(self):
        return "TestView get methosdfsdfd"
