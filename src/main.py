import time
import re
from CalidadAireCrawler import CalidadAireCrawler
from src.CalidadAireScrapper import CalidadAireScrapper
from src.persist.CsvPersistor import CsvPersistor


print 'Scraping datos de calidad de aire de Espana'

start_time = time.time()
output_file = "calidad_aire.persist"

crawler = CalidadAireCrawler()
pages_regiones = crawler.crawl()

scraper = CalidadAireScrapper(pages_regiones)
region_table = scraper.scrap()

csv_persistor = CsvPersistor(region_table, output_file)
csv_persistor.persist()

end_time = time.time()
print "Tiempo de ejecucion: " + str(round((end_time - start_time), 2)) + " segundos"
