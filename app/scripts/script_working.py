import sys

class SimplesTaxCalculator():
    def __init__(self, revenues_twelve_months, attachment, payroll_twelve_months, revenue_month, revenue_month_retention):
        self.ANEXOIII = {   'faixa1': [0.060, 0     , 0.3350 ],
                            'faixa2': [0.112, 9360  , 0.3200 ],
                            'faixa3': [0.135, 17640 , 0.3250 ],
                            'faixa4': [0.160, 35640 , 0.3250 ],
                            'faixa5': [0.210, 125640, 0.3350 ],
                            'faixa6': [0.330, 648000, 0.0000 ]}

        self.ANEXOV =   {   'faixa1': [0.155, 0     , 0.14000 ],
                            'faixa2': [0.180, 4500  , 0.17000 ],
                            'faixa3': [0.195, 9900  , 0.19000 ],
                            'faixa4': [0.205, 17100 , 0.21000 ],
                            'faixa5': [0.230, 62100 , 0.23500 ],
                            'faixa6': [0.305, 540000, 0.00000 ]}

        self.revenues_twelve_months = float(revenues_twelve_months)
        self.payroll = float(payroll_twelve_months)
        self.revenue_month = float(revenue_month)
        self.revenue_month_retention = float(revenue_month_retention)
        self.attachment = getattr(self, attachment) if (self.payroll / self.revenues_twelve_months) < 0.28 else getattr(self, 'ANEXOIII')
        self.tax_range = self.get_tax_range_simple()
        self.rate = float(self.attachment['faixa' + self.tax_range][0])
        self.deduction = float(self.attachment['faixa' + self.tax_range][1])
        self.issqn_porcentage = float(self.attachment['faixa' + self.tax_range][2])
        self.effective_rate = float(self.get_effective_rate())
        self.effective_rate_with_retention = float(self.get_effective_rate_with_retention())

    def get_tax_range_simple(self):
        if (self.revenues_twelve_months <= 180000):
            tax_range_simple = '1'
        elif (self.revenues_twelve_months <= 360000):
            tax_range_simple = '2'
        elif (self.revenues_twelve_months <= 720000):
            tax_range_simple = '3'
        elif (self.revenues_twelve_months <= 1800000):
            tax_range_simple = '4'
        elif (self.revenues_twelve_months <= 3600000):
            tax_range_simple = '5'
        elif (self.revenues_twelve_months <= 4800000):
            tax_range_simple = '6'
        else:
            sys.exit('Excluída')
        return tax_range_simple

    def get_effective_rate(self):
        effective_rate = ( ( self.revenues_twelve_months * self.rate ) - self.deduction ) / self.revenues_twelve_months
        effective_rate = format(effective_rate * 100, '.2f')
        return effective_rate

    def get_effective_rate_with_retention(self):
        effective_rate_with_retention = self.effective_rate - ( self.effective_rate * self.issqn_porcentage )
        effective_rate_with_retention = format( effective_rate_with_retention, '.2f' )
        return effective_rate_with_retention

    def calculate_tax(self):
        tax_without_retention = ( self.revenue_month - self.revenue_month_retention ) * self.effective_rate
        tax_with_retention = self.revenue_month_retention * self.effective_rate_with_retention
        total_tax = tax_without_retention + tax_with_retention
        return total_tax


faturamento_12meses = 180000
anexo = "ANEXOV"
folha_pagamento_12meses = 50400
faturamento_mes = 20000
faturamento_mes_retenção = 10000

# teste 
app = SimplesTaxCalculator(faturamento_12meses, anexo, folha_pagamento_12meses, faturamento_mes, faturamento_mes_retenção)
print(app.get_effective_rate())
print(app.get_effective_rate_with_retention())
print(app.calculate_tax())