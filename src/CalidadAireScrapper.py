import bs4

from src.table.WebTable import WebTable


class CalidadAireScrapper:

    def __init__(self):
        self.url = "http://www.eltiempo.es"

    def scrap(self, pages_regiones):

        print 'Leyendo datos de paginas de regiones'

        for page_region in pages_regiones:
            bs = bs4.BeautifulSoup(page_region, 'html.parser')
            region = bs.select_one('div.pollution_table > mod__table mod__table-responsive mod__table-pollution > tbody > tr > th').text
            table_rows = bs.select('div.pollution_table > mod__table mod__table-responsive mod__table-pollution > tbody > tr > th.data_visible')
            table_values = WebTable(region, table_rows)
            print table_rows

