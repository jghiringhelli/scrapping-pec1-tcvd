import time

from src.persist.CsvPersistor import CsvPersistor
from src.CalidadAireCrawler import CalidadAireCrawler
from src.CalidadAireScrapper import CalidadAireScrapper
from src.RobotsChecker import RobotsChecker

print 'Scraping datos de calidad de aire de Espana'

start_time = time.time()
output_file = "calidad_aire.csv"
user_agent = "uoc_web_crawler"
url = "http://www.eltiempo.es"

# Chequeando que robots.txt no nos bloquea
robotsChecker = RobotsChecker(url, user_agent)
if robotsChecker.checkRobots():
    # Obtener la pagina princial, parsear los vinculos de las paginas de cada region y devolver los DOM
    crawler = CalidadAireCrawler(url, user_agent)
    pages_regiones = crawler.crawl()

    # Dentro de cada documento de region, parsear los datos necesarios y poblar los objetos de tablas, RegionTable
    scraper = CalidadAireScrapper(pages_regiones)
    region_tables = scraper.scrap()

    # Con los datos de las tablas, persistir en CSV los datos agregando a la planilla existente
    csv_persistor = CsvPersistor(region_tables, output_file)
    csv_persistor.persist()

    end_time = time.time()
    print "Tiempo de ejecucion: " + str(round((end_time - start_time), 2)) + " segundos"
else:
    print 'No se puede extraer datos automaticamente en la pagina ' + url
