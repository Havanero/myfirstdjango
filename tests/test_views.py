import unittest2 as unittest2


class TestViews(unittest2.TestCase):
    def test001(self):
        data = {'url': 'https://www.cubanofm.com/item/charity_paint_details/1', 'user_name': 'Nelson Braga'}
        item_id, page = self.extract_page_id(data)
        print(item_id)
        print(self.return_page_id(item_id, page))
        charity_id, graphic_id, painting_id = self.return_page_id(item_id, page)
        print("painting id", painting_id)
        print("graphic id", graphic_id)
        print("charity id", charity_id)
        pass

    @staticmethod
    def return_page_id(item_id, page):
        painting_id = None
        graphic_id = None
        charity_id = None
        if 'paint_details' == page:
            assert page == 'paint_details'
            painting_id = item_id
        if 'graphic_paint_details' == page:
            assert page == 'graphic_paint_details'
            graphic_id = item_id
        if 'charity_paint_details' == page:
            assert page == 'charity_paint_details'
            charity_id = item_id
        return charity_id, graphic_id, painting_id

    @staticmethod
    def extract_page_id(data):
        # print(data[-1:].isdigit())
        url = str(data.get('url')).split("/")
        if url[len(url) - 1].isdigit():
            page_name = (url[len(url) - 1])
            item_id = (url[len(url) - 2])
        else:
            page_name = (url[len(url) - 2])
            item_id = (url[len(url) - 3])

        return page_name, item_id
