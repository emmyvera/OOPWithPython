from fpdf import FPDF

class Bill:
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period        

class Flatmate:
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    
    def pays(self, bill, flatmate=None, flatmates=[]):
        
        if len(flatmates) != 0:
            total_period = 0

            for i in flatmates:
                total_period=+i.days_in_house            
            price = (self.days_in_house/(total_period+self.days_in_house)) * bill.amount
            return price
        
        else:
            total_period = self.days_in_house + flatmate.days_in_house
            price = (self.days_in_house/(total_period+self.days_in_house)) * bill.amount
            return price

class PDFReport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, flatmates=[],):

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=100, h=40, txt='Flatmates Bill', border=1, align='C', ln=1)

        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period:', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.output(self.filename)



if __name__ == '__main__':
    the_bill = Bill(amount=120, period=30)

    john = Flatmate(name='John', days_in_house=30)
    jane = Flatmate(name='Jane', days_in_house=30)
    furstina = Flatmate(name='Furstina', days_in_house=30)
    
    report = PDFReport('Test.pdf')

    report.generate(bill=the_bill)

    print(john.pays(bill=the_bill, flatmate=jane))
