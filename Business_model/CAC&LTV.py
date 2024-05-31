# Расчет CAC к LTV
def calculate_cac_to_ltv(cac, ltv):
    return cac / ltv

cac = 100  # CAC в долларах
ltv = 500  # LTV в долларах

cac_to_ltv_ratio = calculate_cac_to_ltv(cac, ltv)
print(f"Соотношение CAC к LTV составляет {cac_to_ltv_ratio}")


"""
Соотношение CAC к LTV является ключевым показателем для 
оценки эффективности стратегии привлечения клиентов. Оно позволяет бизнесу определить,
 насколько выгодно привлекать клиентов и насколько быстро окупаются маркетинговые затраты. Общепринято считать,
что CAC должен быть ниже LTV, идеально - в 3-5 раз ниже.
"""
