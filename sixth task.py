class Main:
    def init(self):
        self.user1 = input('Введите имя героя: ')
        self.user2 = input('Введите название костюма: ')
        self.user3 = input('Введите название борта: ')
        self.user4 = input('Введите наименование планеты: ')

    def str(self):
        return f'Командир {self.user1} стоял возле своего {self.user2}, в ремонтном отсеке корабля {self.user3}.\n' \
               f'Последние приготовления к высадке на планету {self.user4} подходили к концу\nи вскоре именно ему ' \
               f'было суждено возглавить первую атаку кланов на мир внутренней сферы...'


a = Main()
print(a)