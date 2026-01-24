def refuel_cistern(self):
    new_volume = cistern['current_volume'] + liters
    if new_volume > cistern['max_volume']:
        print(f"Превышение максимального объема! Максимум: {cistern['max_volume']}л")
        return
    self.cisterns[cistern_id]['current_volume'] = new_volume
    self.log_operation('REFUEL', f"Цистерна {cistern_id}, добавлено {liters}л")