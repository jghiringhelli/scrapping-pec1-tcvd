import csv

class CsvPersistor:

    def __init__(self, region_tables, output_file):
        self.region_tables = region_tables
        self.output_file = output_file

    def persist(self):
        print ('Persistiendo datos en CSV de paginas de regiones')
        self.__persist_header__()
        for region_table in self.region_tables:
            region = region_table.region
            for region_row in region_table.region_rows:
                self.__persist_row__(region,region_row)

    def __persist_row__(self, region,region_row):
        ICA = region_row.ICA
        hora=  region_row.hora
        estacion=  region_row.estacion
        O3 = region_row.O3
        NO2 = region_row.NO2
        SO2 = region_row.SO2
        pm25 = region_row.pm25
        pm10 = region_row.pm10
        co = region_row.co
        data = [region, hora, estacion, ICA, O3, NO2, SO2, pm25, pm10, co]
        with open("../data/" + self.output_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
        csv_file.close()
   
    
    def __persist_header__(self):
        data = ['region', 'hora_publicacion', 'estacion', 'ica', 'o3', 'no2', 'so2', 'pm25', 'pm10', 'co']
        with open("../data/" + self.output_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
        csv_file.close()

