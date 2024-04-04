class EventExtractor:
    def __init__(self, strategy):
        self.strategy = strategy

    def extract(self):
        return self.strategy.extract_events()
