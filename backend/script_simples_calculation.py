import sys

ANEXOIII = { 'faixa1': [0.060, 0     ],
             'faixa2': [0.112, 9360  ],
             'faixa3': [0.135, 17640 ],
             'faixa4': [0.160, 35640 ],
             'faixa5': [0.210, 125640],
             'faixa6': [0.330, 648000],}

ANEXOV =   { 'faixa1': [0.155, 0     ],
             'faixa2': [0.180, 4500  ],
             'faixa3': [0.195, 9900  ],
             'faixa4': [0.205, 17100 ],
             'faixa5': [0.230, 62100 ],
             'faixa6': [0.305, 540000],}

revenues_twelve_months = input('Valor faturamento últimos 12 meses? ')

# Validação do input
revenues_twelve_months = float(revenues_twelve_months)

def get_tax_range_simple(revenues_twelve_months):
    if (revenues_twelve_months < 180000):
        tax_range_simple = '1'
    elif (revenues_twelve_months < 360000):
        tax_range_simple = '2'
    elif (revenues_twelve_months < 720000):
        tax_range_simple = '3'
    elif (revenues_twelve_months < 1800000):
        tax_range_simple = '4'
    elif (revenues_twelve_months < 3600000):
        tax_range_simple = '5'
    elif (revenues_twelve_months < 4800000):
        tax_range_simple = '6'
    else:
        sys.exit('Excluída')
    return tax_range_simple

def get_effective_rate(revenues_twelve_months):
    tax_range = get_tax_range_simple(revenues_twelve_months)
    deduction = ANEXOIII['faixa' + tax_range][1]
    rate = ANEXOIII['faixa' + tax_range][0]
    effective_rate = ( ( revenues_twelve_months * rate ) - deduction ) / revenues_twelve_months
    return effective_rate


