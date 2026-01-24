import json
import os
from datetime import datetime

class FuelStation:
    def __init__(self):
        """Инициализация объекта заправочной станции с начальными значениями"""
        # Словарь для хранения данных о цистернах
        self.cisterns = {}
        
        # Цены на различные виды топлива (в рублях за литр)
        self.fuel_prices = {
            'AI-92': 47.50,
            'AI-95': 51.20,
            'AI-98': 58.30,
            'DT': 56.00  # Дизельное топливо
        }
        
        # Словарь для хранения данных о колонках
        self.pumps = {}
        
        # Общий баланс станции
        self.balance = 0.0
        
        # Статистика работы станции
        self.stats = {
            'cars_served': 0,  # Количество обслуженных автомобилей
            'fuel_sold': {'AI-92': 0, 'AI-95': 0, 'AI-98': 0, 'DT': 0},  # Продано топлива по типам
            'income_by_fuel': {'AI-92': 0, 'AI-95': 0, 'AI-98': 0, 'DT': 0}  # Доход по типам топлива
        }
        
        # История операций на станции
        self.history = []
        
        # Флаг аварийного режима (False - нормальный режим, True - аварийный)
        self.emergency_mode = False
        
        # Загрузка начальных данных
        self.initialize_data()
    
    def initialize_data(self):
        """Инициализация начальных данных станции согласно техническому заданию"""
        
        # Инициализация цистерн с начальными значениями
        self.cisterns = {
            'AI-92_1': {
                'type': 'AI-92',
                'max_volume': 20000,       # Максимальный объем (л)
                'current_volume': 12400,   # Текущий объем (л)
                'enabled': True,          # Статус работы (True - включена)
                'min_level': 1000         # Минимальный уровень для работы (л)
            },
            'AI-95_1': {
                'type': 'AI-95',
                'max_volume': 20000,
                'current_volume': 9800,
                'enabled': True,
                'min_level': 1000
            },
            'AI-95_2': {
                'type': 'AI-95',
                'max_volume': 20000,
                'current_volume': 1200,    # Низкий уровень - цистерна отключена
                'enabled': False,
                'min_level': 1000
            },
            'AI-98_1': {
                'type': 'AI-98',
                'max_volume': 15000,
                'current_volume': 10000,
                'enabled': False,          # Отключена вручную
                'min_level': 1000
            },
            'DT_1': {
                'type': 'DT',
                'max_volume': 25000,
                'current_volume': 15600,
                'enabled': True,
                'min_level': 1000
            }
        }
        
        # Инициализация колонок с привязкой к цистернам
        self.pumps = {
            1: {'fuels': {'AI-95': 'AI-95_1', 'AI-92': 'AI-92_1'}},
            2: {'fuels': {'AI-95': 'AI-95_1', 'AI-92': 'AI-92_1'}},
            3: {'fuels': {'AI-95': 'AI-95_1', 'AI-92': 'AI-92_1', 'AI-98': 'AI-98_1', 'DT': 'DT_1'}},
            4: {'fuels': {'AI-95': 'AI-95_1', 'AI-92': 'AI-92_1', 'DT': 'DT_1'}},
            5: {'fuels': {'AI-95': 'AI-95_2', 'AI-92': 'AI-92_1', 'AI-98': 'AI-98_1', 'DT': 'DT_1'}},
            6: {'fuels': {'AI-95': 'AI-95_2', 'AI-92': 'AI-92_1', 'AI-98': 'AI-98_1', 'DT': 'DT_1'}},
            7: {'fuels': {'AI-95': 'AI-95_2', 'DT': 'DT_1'}},
            8: {'fuels': {'AI-95': 'AI-95_2', 'DT': 'DT_1'}}
        }
    
    def save_data(self):
        """Сохранение текущего состояния станции в JSON файл"""
        data = {
            'cisterns': self.cisterns,
            'balance': self.balance,
            'stats': self.stats,
            'history': self.history,
            'emergency_mode': self.emergency_mode
        }
        with open('station_data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def load_data(self):
        """Загрузка состояния станции из JSON файла (если он существует)"""
        if os.path.exists('station_data.json'):
            with open('station_data.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Загружаем данные или используем значения по умолчанию
                self.cisterns = data.get('cisterns', self.cisterns)
                self.balance = data.get('balance', 0.0)
                self.stats = data.get('stats', self.stats)
                self.history = data.get('history', [])
                self.emergency_mode = data.get('emergency_mode', False)
    
    def log_operation(self, operation_type, details):
        """Логирование операции в историю с сохранением в файл"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'timestamp': timestamp,
            'type': operation_type,  # Тип операции (SALE, REFUEL, TRANSFER и т.д.)
            'details': details       # Детали операции
        }
        self.history.append(entry)
        self.save_data()  # Сохраняем после каждой операции
    
    def check_low_levels(self):
        """Проверка и автоматическое отключение цистерн с низким уровнем топлива"""
        low_level_cisterns = []
        for cistern_id, cistern in self.cisterns.items():
            # Проверяем, достигнут ли минимальный уровень
            if cistern['current_volume'] <= cistern['min_level']:
                # Автоматически отключаем, если цистерна еще включена
                if cistern['enabled']:
                    cistern['enabled'] = False
                    self.log_operation('AUTO_DISABLE', f"Цистерна {cistern_id} отключена из-за низкого уровня")
                low_level_cisterns.append(cistern_id)
        return low_level_cisterns
    
    def display_menu(self):
        """Отображение главного меню программы"""
        print("=" * 40)
        print("АЗС <<СеверНефть>>")
        print("Система управления заправочной станцией")
        print("=" * 40)
        
        # Проверяем и отображаем цистерны с низким уровнем
        low_level_cisterns = self.check_low_levels()
        if low_level_cisterns:
            print("\nВНИМАНИЕ!")
            print("Обнаружены отключённые цистерны:")
            for cistern_id in low_level_cisterns:
                cistern = self.cisterns[cistern_id]
                print(f" - {cistern_id} (низкий уровень топлива)")
        
        print("-" * 40)
        print("Выберите действие:")
        print("1) Обслужить клиента (касса)")
        print("2) Проверить состояние цистерн")
        print("3) Оформить пополнение топлива")
        print("4) Баланс и статистика")
        print("5) История операций")
        print("6) Перекачка топлива между цистернами")
        print("7) Включение / отключение цистерн")
        print("8) Состояние колонок")
        print("9) EMERGENCY - аварийная ситуация")
        print("0) Выход")
    
    def serve_customer(self):
        """Обработка запроса на обслуживание клиента"""
        print("--- Обслуживание клиента ---")
        
        # Проверка аварийного режима
        if self.emergency_mode:
            print("Ошибка: Станция находится в аварийном режиме!")
            input("Нажмите Enter для возврата в меню...")
            return
        
        # Отображение доступных колонок
        print("Доступные колонки:")
        for pump_num in sorted(self.pumps.keys()):
            available_fuels = []
            # Проверяем, какие виды топлива доступны на колонке
            for fuel_type, cistern_id in self.pumps[pump_num]['fuels'].items():
                if self.cisterns[cistern_id]['enabled']:
                    available_fuels.append(fuel_type)
            
            # Показываем только колонки с доступным топливом
            if available_fuels:
                print(f"{pump_num}) Колонка {pump_num}")
        
        try:
            # Выбор колонки
            pump_choice = int(input("Выберите колонку: "))
            if pump_choice not in self.pumps:
                print("Неверный номер колонки!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            pump = self.pumps[pump_choice]
            available_fuels = {}
            
            print(f"Колонка {pump_choice}")
            print("Доступные виды топлива:")
            
            # Отображение доступных видов топлива на выбранной колонке
            option_num = 1
            for fuel_type, cistern_id in pump['fuels'].items():
                cistern = self.cisterns[cistern_id]
                if cistern['enabled']:
                    available_fuels[option_num] = (fuel_type, cistern_id)
                    print(f"{option_num}) {fuel_type} (цистерна {cistern_id})")
                    option_num += 1
                else:
                    print(f"{option_num}) {fuel_type} (цистерна {cistern_id}) - НЕДОСТУПНО")
                    option_num += 1
            
            # Выбор типа топлива
            fuel_choice = int(input("Выберите тип топлива: "))
            if fuel_choice not in available_fuels:
                print("Неверный выбор топлива!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            fuel_type, cistern_id = available_fuels[fuel_choice]
            
            # Ввод количества литров
            liters = float(input("Введите количество литров: "))
            
            if liters <= 0:
                print("Количество литров должно быть положительным!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Проверка наличия достаточного количества топлива
            cistern = self.cisterns[cistern_id]
            if liters > cistern['current_volume']:
                print("Недостаточно топлива в цистерне!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Расчет стоимости
            price = liters * self.fuel_prices[fuel_type]
            print(f"\nСтоимость:\n{liters} л × {self.fuel_prices[fuel_type]:.2f} ₽ = {price:.2f} ₽")
            
            # Подтверждение оплаты
            confirm = input("Подтвердить оплату? (y/n): ").lower()
            if confirm == 'y':
                # Списываем топливо из цистерны
                self.cisterns[cistern_id]['current_volume'] -= liters
                
                # Обновляем статистику и баланс
                self.balance += price
                self.stats['cars_served'] += 1
                self.stats['fuel_sold'][fuel_type] += liters
                self.stats['income_by_fuel'][fuel_type] += price
                
                # Логируем операцию продажи
                self.log_operation('SALE', f"Колонка {pump_choice}, {fuel_type}, {liters}л, {price:.2f}₽")
                
                print("Операция выполнена успешно.")
                print("Спасибо за покупку!")
            else:
                print("Оплата отменена.")
        
        except ValueError:
            print("Неверный ввод!")
        
        input("Нажмите Enter для возврата в меню...")
    
    def check_cisterns(self):
        """Отображение текущего состояния всех цистерн"""
        print("--- Состояние цистерн ---")
        print("Доступные цистерны:")
        
        for cistern_id, cistern in self.cisterns.items():
            status = "ВКЛ" if cistern['enabled'] else "ВЫКЛ"
            warning = ""
            if cistern['current_volume'] <= cistern['min_level']:
                warning = " (ниже порога)"
            print(f"{cistern_id} | {cistern['current_volume']} / {cistern['max_volume']} л | {status}{warning}")
        
        input("Нажмите Enter для возврата в меню...")
    
    def refuel_cistern(self):
        """Пополнение цистерны топливом"""
        print("--- Оформить пополнение топлива ---")
        
        # Отображение доступных типов топлива
        print("Доступные типы топлива:")
        fuel_types = set(cistern['type'] for cistern in self.cisterns.values())
        type_to_ids = {}
        for i, fuel_type in enumerate(sorted(fuel_types), 1):
            type_to_ids[i] = fuel_type
            print(f"{i}) {fuel_type}")
        
        try:
            # Выбор типа топлива
            type_choice = int(input("Выберите тип топлива: "))
            if type_choice not in type_to_ids:
                print("Неверный выбор!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            selected_type = type_to_ids[type_choice]
            
            # Фильтрация цистерн по выбранному типу топлива
            available_cisterns = {cid: cistern for cid, cistern in self.cisterns.items() 
                                if cistern['type'] == selected_type}
            
            # Отображение доступных цистерн выбранного типа
            print(f"Доступные цистерны для {selected_type}:")
            id_to_cistern = {}
            for i, (cistern_id, cistern) in enumerate(available_cisterns.items(), 1):
                id_to_cistern[i] = cistern_id
                print(f"{i}) {cistern_id}")
            
            # Выбор конкретной цистерны
            cistern_choice = int(input("Выберите цистерну: "))
            if cistern_choice not in id_to_cistern:
                print("Неверный выбор!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            cistern_id = id_to_cistern[cistern_choice]
            
            # Ввод количества литров для пополнения
            liters = float(input("Введите количество литров для добавления: "))
            
            if liters <= 0:
                print("Количество литров должно быть положительным!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Проверка на превышение максимального объема
            cistern = self.cisterns[cistern_id]
            new_volume = cistern['current_volume'] + liters
            
            if new_volume > cistern['max_volume']:
                print(f"Превышение максимального объема! Максимум: {cistern['max_volume']}л")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Обновление объема цистерны и логирование
            self.cisterns[cistern_id]['current_volume'] = new_volume
            self.log_operation('REFUEL', f"Цистерна {cistern_id}, добавлено {liters}л")
            
            print(f"Топливо успешно добавлено в цистерну {cistern_id}")
        
        except ValueError:
            print("Неверный ввод!")
        
        input("Нажмите Enter для возврата в меню...")
    
    def show_balance_stats(self):
        """Отображение баланса и статистики работы станции"""
        print("--- Баланс и статистика ---")
        print(f"Обслужено автомобилей: {self.stats['cars_served']}")
        print(f"Общий доход: {self.balance:.2f} ₽")
        print("\nПродано топлива:")
        for fuel_type in ['AI-92', 'AI-95', 'AI-98', 'DT']:
            liters = self.stats['fuel_sold'][fuel_type]
            income = self.stats['income_by_fuel'][fuel_type]
            print(f"{fuel_type:<6} - {liters:>6.0f} л ({income:>8.0f} ₽)")
        
        input("Нажмите Enter для возврата в меню...")
    
    def show_history(self):
        """Отображение последних операций из истории"""
        print("--- История операций ---")
        if not self.history:
            print("История операций пуста.")
        else:
            # Показываем последние 10 операций (сначала новые)
            for entry in reversed(self.history[-10:]):
                print(f"[{entry['timestamp']}] {entry['type']}: {entry['details']}")
        
        input("Нажмите Enter для возврата в меню...")
    
    def transfer_fuel(self):
        """Перекачка топлива между цистернами одного типа"""
        print("--- Перекачка топлива ---")
        
        # Группировка цистерн по типам топлива
        fuel_groups = {}
        for cistern_id, cistern in self.cisterns.items():
            fuel_type = cistern['type']
            if fuel_type not in fuel_groups:
                fuel_groups[fuel_type] = []
            fuel_groups[fuel_type].append(cistern_id)
        
        # Отображение доступных типов топлива для перекачки
        print("Доступные типы топлива для перекачки:")
        for i, fuel_type in enumerate(fuel_groups.keys(), 1):
            print(f"{i}) {fuel_type}")
        
        try:
            # Выбор типа топлива
            choice = int(input("Выберите тип топлива: ")) - 1
            fuel_types_list = list(fuel_groups.keys())
            if choice < 0 or choice >= len(fuel_types_list):
                print("Неверный выбор!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            fuel_type = fuel_types_list[choice]
            cisterns_of_type = fuel_groups[fuel_type]
            
            # Отображение цистерн выбранного типа
            print(f"Цистерны с {fuel_type}:")
            for i, cistern_id in enumerate(cisterns_of_type, 1):
                cistern = self.cisterns[cistern_id]
                print(f"{i}) {cistern_id} | {cistern['current_volume']} / {cistern['max_volume']} л")
            
            # Выбор цистерны-источника и цистерны-приемника
            source_choice = int(input("Выберите цистерну-источник: ")) - 1
            dest_choice = int(input("Выберите цистерну-приемник: ")) - 1
            
            # Проверка корректности выбора
            if source_choice < 0 or source_choice >= len(cisterns_of_type) or \
               dest_choice < 0 or dest_choice >= len(cisterns_of_type) or \
               source_choice == dest_choice:
                print("Неверный выбор!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            source_id = cisterns_of_type[source_choice]
            dest_id = cisterns_of_type[dest_choice]
            
            # Ввод количества литров для перекачки
            liters = float(input("Введите количество литров для перекачки: "))
            
            if liters <= 0:
                print("Количество литров должно быть положительным!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Проверка достаточности топлива в источнике
            source_cistern = self.cisterns[source_id]
            dest_cistern = self.cisterns[dest_id]
            
            if liters > source_cistern['current_volume']:
                print("Недостаточно топлива в источнике!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Проверка свободного места в приемнике
            if dest_cistern['current_volume'] + liters > dest_cistern['max_volume']:
                print("Превышение максимального объема в приемнике!")
                input("Нажмите Enter для возврата в меню...")
                return
            
            # Выполнение перекачки
            self.cisterns[source_id]['current_volume'] -= liters
            self.cisterns[dest_id]['current_volume'] += liters
            
            # Логирование операции перекачки
            self.log_operation('TRANSFER', f"Из {source_id} в {dest_id}, {liters}л")
            print("Перекачка выполнена успешно!")
        
        except ValueError:
            print("Неверный ввод!")
        
        input("Нажмите Enter для возврата в меню...")
    
    def manage_cisterns(self):
        """Ручное управление состоянием цистерн (включение/отключение)"""
        print("--- Управление цистернами ---")
        print("Доступные действия:")
        print("1) Включить цистерну")
        print("2) Отключить цистерну")
        
        try:
            action = int(input("> "))
            
            if action == 1:
                # Включение цистерны
                # Находим отключенные цистерны с достаточным уровнем топлива
                disabled_cisterns = [cid for cid, cistern in self.cisterns.items() 
                                   if not cistern['enabled'] and cistern['current_volume'] > cistern['min_level']]
                
                if not disabled_cisterns:
                    print("Нет цистерн для включения (все включены или уровень слишком низкий).")
                    input("Нажмите Enter для возврата в меню...")
                    return
                
                print("Цистерны, доступные для включения:")
                for i, cistern_id in enumerate(disabled_cisterns, 1):
                    cistern = self.cisterns[cistern_id]
                    print(f"{i}) {cistern_id} | {cistern['current_volume']} / {cistern['max_volume']} л")
                
                choice = int(input("Выберите цистерну: ")) - 1
                if 0 <= choice < len(disabled_cisterns):
                    cistern_id = disabled_cisterns[choice]
                    self.cisterns[cistern_id]['enabled'] = True
                    self.log_operation('ENABLE', f"Цистерна {cistern_id} включена")
                    print(f"Цистерна {cistern_id} успешно включена.")
                else:
                    print("Неверный выбор!")
            
            elif action == 2:
                # Отключение цистерны
                # Находим включенные цистерны
                enabled_cisterns = [cid for cid, cistern in self.cisterns.items() if cistern['enabled']]
                
                if not enabled_cisterns:
                    print("Нет цистерн для отключения.")
                    input("Нажмите Enter для возврата в меню...")
                    return
                
                print("Цистерны, доступные для отключения:")
                for i, cistern_id in enumerate(enabled_cisterns, 1):
                    cistern = self.cisterns[cistern_id]
                    print(f"{i}) {cistern_id} | {cistern['current_volume']} / {cistern['max_volume']} л")
                
                choice = int(input("Выберите цистерну: ")) - 1
                if 0 <= choice < len(enabled_cisterns):
                    cistern_id = enabled_cisterns[choice]
                    self.cisterns[cistern_id]['enabled'] = False
                    self.log_operation('DISABLE', f"Цистерна {cistern_id} отключена")
                    print(f"Цистерна {cistern_id} успешно отключена.")
                else:
                    print("Неверный выбор!")
            else:
                print("Неверный выбор!")
        
        except ValueError:
            print("Неверный ввод!")
        
        input("Нажмите Enter для возврата в меню...")
    
    def show_pumps_status(self):
        """Отображение текущего состояния всех колонок"""
        print("--- Состояние колонок ---")
        
        for pump_num in sorted(self.pumps.keys()):
            print(f"Колонка {pump_num}")
            print("  Доступные виды топлива:")
            
            # Отображение доступных видов топлива на каждой колонке
            for fuel_type, cistern_id in self.pumps[pump_num]['fuels'].items():
                cistern = self.cisterns[cistern_id]
                status = "РАБОТАЕТ" if cistern['enabled'] else "НЕ РАБОТАЕТ"
                print(f"    {fuel_type} -> {cistern_id} ({status})")
            print()
        
        input("Нажмите Enter для возврата в меню...")
    
    def emergency_mode_handler(self):
        """Обработка аварийного режима работы станции"""
        print("--- EMERGENCY - аварийная ситуация ---")
        print("ВНИМАНИЕ! Все цистерны будут заблокированы!")
        
        # Подтверждение активации аварийного режима
        confirm = input("Подтвердить аварию? (y/n): ").lower()
        
        if confirm == 'y':
            # Блокировка всех цистерн
            for cistern_id, cistern in self.cisterns.items():
                if cistern['enabled']:
                    cistern['enabled'] = False
                    self.log_operation('EMERGENCY_DISABLE', f"Цистерна {cistern_id} заблокирована при аварии")
            
            # Активация аварийного режима
            self.emergency_mode = True
            self.log_operation('EMERGENCY', "Аварийная ситуация активирована")
            print("Аварийный режим активирован. Заправка остановлена.")
        else:
            print("Авария отменена.")
            return
        
        # Выход из аварийного режима
        exit_confirm = input("Выйти из аварийного режима? (y/n): ").lower()
        if exit_confirm == 'y':
            self.emergency_mode = False
            self.log_operation('EMERGENCY_END', "Аварийный режим завершен")
            print("Аварийный режим завершен.")
        
        input("Нажмите Enter для возврата в меню...")
    
    def run(self):
        """Главный цикл работы программы"""
        # Загрузка сохраненных данных
        self.load_data()
        
        while True:
            # Отображение меню
            self.display_menu()
            try:
                # Обработка выбора пользователя
                choice = int(input("> "))
                
                if choice == 0:
                    print("Выход из программы...")
                    break
                elif choice == 1:
                    self.serve_customer()
                elif choice == 2:
                    self.check_cisterns()
                elif choice == 3:
                    self.refuel_cistern()
                elif choice == 4:
                    self.show_balance_stats()
                elif choice == 5:
                    self.show_history()
                elif choice == 6:
                    self.transfer_fuel()
                elif choice == 7:
                    self.manage_cisterns()
                elif choice == 8:
                    self.show_pumps_status()
                elif choice == 9:
                    self.emergency_mode_handler()
                else:
                    print("Неверный выбор! Пожалуйста, выберите от 0 до 9.")
                    input("Нажмите Enter для продолжения...")
                    
            except ValueError:
                print("Неверный ввод! Пожалуйста, введите число.")
                input("Нажмите Enter для продолжения...")

# Точка входа в программу
if __name__ == "__main__":
    # Создание объекта заправочной станции
    station = FuelStation()
    # Запуск главного цикла
    station.run()