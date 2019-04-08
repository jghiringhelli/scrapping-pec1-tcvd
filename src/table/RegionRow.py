from src import util


class RegionRow:
    def __init__(self, region_row_tag):
        self.region_row_tag = region_row_tag
        self.ICA = self.__get_value__('td[data-visible]', 'span[class*="aqi aqi"]')
        self.O3 = self.__get_value__('td[data-title="O3"]', 'span[class="data"]')
        self.NO2 = self.__get_value__('td[data-title="NO2"]', 'span[class="data"]')
        self.SO2 = self.__get_value__('td[data-title="SO2"]', 'span[class="data"]')
        self.pm25 = self.__get_value__('td[data-title="PM25"]', 'span[class="data"]')
        self.pm10 = self.__get_value__('td[data-title="PM"]', 'span[class="data"]')
        self.co = self.__get_value__('td[data-title="CO"]', 'span[class="data"]')

    def __get_value__(self, column, value):
        if self.region_row_tag.select_one(column + ' span[class="info value_null"]'):
            return ''
        return util.cleantext(self.region_row_tag.select_one(column + ' > ' + value).text.rstrip())
