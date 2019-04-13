import csv
import os.path

class CsvPersistor:

    def __init__(self, region_tables, output_file):
        self.region_tables = region_tables
        self.output_file = output_file

    def persist(self):
        print ('Persistiendo datos en CSV de paginas de regiones')
        self.__persist_header__()
        # Por cada region
        for region_table in self.region_tables:
            region = region_table.region.encode('utf-8')
            # Guardando datos de cade estacion, filas del CSV
            for region_row in region_table.region_rows:
                self.__persist_row__(region, region_row)

    def __persist_row__(self, region, region_row):
        ICA = region_row.ICA.encode('utf-8')
        hora = region_row.hora.encode('utf-8')
        estacion = region_row.estacion.encode('utf-8')
        O3 = region_row.O3.encode('utf-8')
        NO2 = region_row.NO2.encode('utf-8')
        SO2 = region_row.SO2.encode('utf-8')
        pm25 = region_row.pm25.encode('utf-8')
        pm10 = region_row.pm10.encode('utf-8')
        co = region_row.co.encode('utf-8')
        data = [region, hora, estacion, ICA, O3, NO2, SO2, pm25, pm10, co]
        # Anexar datos a planilla csv
        with open("../data/" + self.output_file, 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data)
        csv_file.close()

    def __persist_header__(self):
        data = ['region', 'hora_publicacion', 'estacion', 'ica', 'o3', 'no2', 'so2', 'pm25', 'pm10', 'co']
        [x.encode('utf-8') for x in data]
            # Si el archivo existe no se agrega el encabezado
        if not os.path.isfile("../data/" + self.output_file):
                with open("../data/" + self.output_file, 'a') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(data)
                    csv_file.close()

