from src import util
from src.table.RegionRow import RegionRow


class RegionTable:

    def __init__(self, region_table_tag):
        self.region = util.cleantext(region_table_tag.table.tr.th.text)
        self.hora = self.__get_hora__(region_table_tag)
        self.estacion = util.cleantext(region_table_tag.table.td.find(text=True, recursive=False))
        self.region_rows = []
        region_rows_tags = region_table_tag.select('tr')
        for region_row_tag in region_rows_tags:
            if region_row_tag.select('td'):
                self.region_rows.append(RegionRow(region_row_tag))

    def __get_hora__(self, region_table_tag):
        time = region_table_tag.table.td.select_one('span[class="time"]').text
        return util.cleantext(time)
