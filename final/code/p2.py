def initialize_data(self):
    self.cisterns = {
        'AI-92_1': {
            'type': 'AI-92',
            'max_volume': 20000,
            'current_volume': 12400,
            'enabled': True,
            'min_level': 1000
        },
        'AI-95_1': {
            'type': 'AI-95',
            'max_volume': 20000,
            'current_volume': 9800,
            'enabled': True,
            'min_level': 1000
        },
        # ... остальные цистерны
    }