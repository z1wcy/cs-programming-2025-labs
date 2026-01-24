def serve_customer(self):
    if self.emergency_mode:
        print("Ошибка: Станция находится в аварийном режиме!")
        return
    
    # Выбор колонки
    for pump_num in sorted(self.pumps.keys()):
        available_fuels = []
        for fuel_type, cistern_id in self.pumps[pump_num]['fuels'].items():
            if self.cisterns[cistern_id]['enabled']:
                available_fuels.append(fuel_type)
    
    # Проверка оплаты и списание топлива
    confirm = input("Подтвердить оплату? (y/n): ").lower()
    if confirm == 'y':
        self.cisterns[cistern_id]['current_volume'] -= liters
        self.balance += price
        self.stats['cars_served'] += 1
        self.log_operation('SALE', f"Колонка {pump_choice}, {fuel_type}, {liters}л, {price:.2f}₽")