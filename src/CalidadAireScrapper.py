import bs4

from src import util
from src.table.RegionTable import RegionTable


class CalidadAireScrapper:

    def __init__(self, pages_regiones):
        self.url = "http://www.eltiempo.es"
        self.pages_regiones = pages_regiones

    def scrap(self, ):
        print 'Leyendo datos de paginas de regiones'
        for page_region in self.pages_regiones:
            bs = bs4.BeautifulSoup(page_region, 'html.parser')
            region_table_tag = bs.select_one('div[id="pollution_table"]')
            return RegionTable(region_table_tag)
