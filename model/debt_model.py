
# класс - модель данных для связи с внешним миром
# Миша подредачь тут плез 

class DebtModel():
    def __init__(self):
        self.debtor_id = "0"
        self.cresitor_id="0"
        self.amount = 0
        self.date = "0"
    
    def from_tuple(self, tuple=()):
        if len(tuple)!=5:
            raise Exception("Wrnog tuple ot decode")
        self.debtor_id = tuple[1]
        self.creditor_id = tuple[2]
        self.amount = tuple[3]
        self.date = tuple[4]

        