import csv


class CsvPersistor:

    def __init__(self, region_table, output_file):
        self.region_table = region_table
        self.output_file = output_file

    def persist(self):
        print 'Persistiendo datos en CSV de paginas de regiones'
        region = self.region_table.region
        hora = self.region_table.hora
        estacion = self.region_table.estacion
        for region_row in self.region_table.region_rows:
            self.__persist_row__(region, hora, estacion, region_row)

    def __persist_row__(self, region, hora, estacion, region_row):
        ICA = region_row.ICA
        O3 = region_row.O3
        NO2 = region_row.NO2
        SO2 = region_row.SO2
        pm25 = region_row.pm25
        pm10 = region_row.pm10
        co = region_row.co
        data = [region, hora, estacion, ICA, O3, NO2, SO2, pm25, pm10, co]
        with open("../data/" + self.output_file, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=' ', quotechar='|')
            writer.writerow(data)
        csv_file.close()
