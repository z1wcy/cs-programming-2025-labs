def emergency_mode_handler(self):
    print("ВНИМАНИЕ! Все цистерны будут заблокированы!")
    confirm = input("Подтвердить аварию? (y/n): ").lower()
    
    if confirm == 'y':
        for cistern_id, cistern in self.cisterns.items():
            if cistern['enabled']:
                cistern['enabled'] = False
                self.log_operation('EMERGENCY_DISABLE', f"Цистерна {cistern_id} заблокирована при аварии")
        
        self.emergency_mode = True
        self.log_operation('EMERGENCY', "Аварийная ситуация активирована")