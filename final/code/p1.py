class FuelStation:
    def __init__(self):
        self.cisterns = {}
        self.fuel_prices = {
            'AI-92': 47.50,
            'AI-95': 51.20,
            'AI-98': 58.30,
            'DT': 56.00
        }
        self.pumps = {}
        self.balance = 0.0
        self.stats = {
            'cars_served': 0,
            'fuel_sold': {'AI-92': 0, 'AI-95': 0, 'AI-98': 0, 'DT': 0},
            'income_by_fuel': {'AI-92': 0, 'AI-95': 0, 'AI-98': 0, 'DT': 0}
        }
        self.history = []
        self.emergency_mode = False
        
        self.initialize_data()