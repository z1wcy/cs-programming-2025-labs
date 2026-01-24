def save_data(self):
    data = {
        'cisterns': self.cisterns,
        'balance': self.balance,
        'stats': self.stats,
        'history': self.history,
        'emergency_mode': self.emergency_mode
    }
    with open('station_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)