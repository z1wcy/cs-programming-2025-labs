def transfer_fuel(self):
    # Проверка типа топлива
    if self.cisterns[source_id]['type'] != self.cisterns[dest_id]['type']:
        print("Ошибка: перекачка возможна только между цистернами одного типа!")
        return
    
    # Проверка объемов
    if liters > source_cistern['current_volume']:
        print("Недостаточно топлива в источнике!")
        return
    
    if dest_cistern['current_volume'] + liters > dest_cistern['max_volume']:
        print("Превышение максимального объема в приемнике!")
        return
    
    # Выполнение перекачки
    self.cisterns[source_id]['current_volume'] -= liters
    self.cisterns[dest_id]['current_volume'] += liters
    self.log_operation('TRANSFER', f"Из {source_id} в {dest_id}, {liters}л")