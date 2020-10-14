import sys

class SimplesTaxCalculator():
    def __init__(self, revenues_twelve_months, attachment, payroll_twelve_months, revenue_month):
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
        self.attachment = getattr(self, attachment) if (self.payroll / self.revenues_twelve_months) < 0.28 else getattr(self, 'ANEXOIII')

    def get_tax_range_simple(self):
        if (self.revenues_twelve_months < 180000):
            tax_range_simple = '1'
        elif (self.revenues_twelve_months < 360000):
            tax_range_simple = '2'
        elif (self.revenues_twelve_months < 720000):
            tax_range_simple = '3'
        elif (self.revenues_twelve_months < 1800000):
            tax_range_simple = '4'
        elif (self.revenues_twelve_months < 3600000):
            tax_range_simple = '5'
        elif (self.revenues_twelve_months < 4800000):
            tax_range_simple = '6'
        else:
            sys.exit('Excluída')
        return tax_range_simple

    def get_effective_rate(self):
        tax_range = self.get_tax_range_simple()
        deduction = self.attachment['faixa' + tax_range][1]
        rate = self.attachment['faixa' + tax_range][0]
        rate_with_retention = self.attachment['faixa' + tax_range][2]
        effective_rate = ( ( self.revenues_twelve_months * rate ) - deduction ) / self.revenues_twelve_months
        effective_rate = format(effective_rate * 100, '.2f')
        return effective_rate, rate_with_retention
