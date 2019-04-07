import urllib2
import bs4


class CalidadAireCrawler:

    def __init__(self):
        self.url = "http://www.eltiempo.es"
        self.subdomain = "/calidad-aire"

    def __get_main__page(self, url):
        response = urllib2.urlopen(url)
        page = response.read()
        return page

    def __parse__main__page(self, page):
        bs = bs4.BeautifulSoup(page, 'html.parser')
        table_rows = bs.select('ul.m_pollution-list > li > a')
        links_regiones = []
        for row in table_rows:
            links_regiones.append(self.__create_link_region(row))
        return links_regiones

    def __create_link_region(self, row):
        linkRegion = row['href']
        region = row.span.span.text.rstrip()
        print 'Encontrado link para region ' + region + " " + linkRegion
        return linkRegion

    def __get_pages_regiones(self, links_regiones):
        pages_regiones = []
        for linkRegion in links_regiones:
            pages_regiones.append(self.__get_main__page(linkRegion))
        return pages_regiones

    def crawl(self):

        print 'Leyendo pagina principal'

        paginaPrincipal = self.__get_main__page(self.url + self.subdomain)
        linksRegiones = self.__parse__main__page(paginaPrincipal)
        return self.__get_pages_regiones(linksRegiones)
