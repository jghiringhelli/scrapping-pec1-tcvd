import time
from CalidadAireCrawler import CalidadAireCrawler

print 'Scraping datos de calidad de aire de Espana'

start_time = time.time()

crawler = CalidadAireCrawler()
pages_regiones = crawler.crawl()

end_time = time.time()
print "Tiempo de ejecucion: " + str(round((end_time - start_time), 2)) + " segundos"
