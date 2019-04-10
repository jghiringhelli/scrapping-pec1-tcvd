from src.table.RegionRow import RegionRow


class RegionTable:

    def __init__(self, region_table_tag):
        self.region = region_table_tag.h2.text.replace('Estaciones de ','')
        self.region_rows = []
        region_rows_tags = region_table_tag.select('tr')
        for region_row_tag in region_rows_tags:
            if region_row_tag.select('td'):
                self.region_rows.append(RegionRow(region_row_tag))




