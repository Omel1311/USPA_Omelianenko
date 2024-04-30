import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

# Задаємо ставку податку, середній дохід і податкову знижку
tax_rate = 0.30
average_income = 2000  # середній дохід
tax_credit = 2400  # podatek ulgowy

# Обрахунок podatku przed ulgą
tax_before_credit = average_income * tax_rate

# Efektywny podatek po uwzględnieniu ulgi
effective_tax = max(0, tax_before_credit - tax_credit)

# Wpływ na budżet
if tax_before_credit > tax_credit:
    budget_effect = "Zmniejszenie"
else:
    budget_effect = "Brak zmian" if effective_tax == 0 else "Zmniejszenie"

# Wyświetlenie wyników
print(f"Podatek przed ulgą: {tax_before_credit} LM")
print(f"Efektywny podatek po uldze: {effective_tax} LM")
print(f"Wpływ budżetowy: {budget_effect}")

# Graficzne przedstawienie krzywej Laffera
tax_rates = np.linspace(0, 1, 100)
tax_revenues = 44000000000 * tax_rates / 0.15 * (1 - tax_rates**2)
plt.figure(figsize=(10, 6))
plt.plot(tax_rates, tax_revenues, label='Krzywa Laffera')
plt.xlabel('Stawka podatkowa')
plt.ylabel('Przychody podatkowe')
plt.title('Krzywa Laffera z uwzględnieniem ulgi podatkowej')
plt.axvline(x=0.30, color='red', linestyle='--', label='Stawka podatkowa 30%')
plt.legend()
plt.show()
