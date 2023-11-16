class Author:
    def __init__(self,name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return  sum([contract.royalties for contract in self.contracts()])

class Book:
    def __init__(self,title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):

        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception('author must exist')
        if isinstance(book,Book):
            self.book = book
        else:
            raise Exception('book must exist')
        if isinstance(date, str):
            self.date = date
        else:
            raise Exception('date must be string')
        if isinstance(royalties, int): 
            self.royalties = royalties
        else:
            raise Exception('royalties must be an integer')
        
        Contract.all.append(self)

    def __repr__(self):
        return f"contract: date={self.date}, book={self.book.title}, author={self.author.name}, royalties={self.royalties}"

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]