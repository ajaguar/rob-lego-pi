class Sensor:
    port = None
    
    def __init__(self, port):
        def __init__(self, port):
        assert isinstance(port, Port)
        self._setupPins(port)
        self.port = port;