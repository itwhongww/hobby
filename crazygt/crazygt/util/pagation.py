# -*- coding: utf-8 -*-

class Pagation:

    def __init__(self, page_size, page_num, entitis):
        self.start = (int(page_num) - 1) * int(page_size)
        self.end = self.start + int(page_size)
        self.entitis = entitis
    def total_count(self):
        return len(self.entitis)

    def entity(self):
        return self.entitis[self.start: self.end]
