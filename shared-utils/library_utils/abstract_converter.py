from typing import List


class AbstractConverter:
    def map_do_to_mo(self, item_do):
        pass

    def map_mo_to_do(self, item_mo):
        pass

    def map_add_to_mo(self, item_add):
        pass

    def map_update_to_mo(self, item_old, item_update):
        pass

    def map_list_do_to_list_mo(self, item_do_list: List) -> List:
        return [self.map_do_to_mo(item_do) for item_do in item_do_list]
