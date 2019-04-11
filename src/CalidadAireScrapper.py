import bs4

from src.table.RegionTable import RegionTable


class CalidadAireScrapper:

    def __init__(self, pages_regiones):
        self.pages_regiones = pages_regiones

    def scrap(self):
        print ('Leyendo datos de paginas de regiones')
        region_tables = []
        for page_region in self.pages_regiones:
            bs = bs4.BeautifulSoup(page_region, 'html.parser')
            # Creando el objeo RegionTable con todos los datos necesarios por region, varias filas de datos, usando los bloques de region
            region_table_tag = bs.select_one('article[class="modules m_pollution"]')
            region_tables.append(RegionTable(region_table_tag))
        return region_tables
