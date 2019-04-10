import urllib.request
import bs4



class CalidadAireCrawler:

    def __init__(self):
        self.url = "http://www.eltiempo.es"
        self.subdomain = "/calidad-aire"
        self.min_retries = 3

    def __get_main_page__(self, url, num_retries):
        try:
            response = urllib.request.urlopen(url)
            page = response.read()
        except urllib.error.URLError as e:
            print ('Download error:', e.reason)
            page = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    page = self.__get_main_page__(url, num_retries - 1)
        return page

    def __parse_main_page__(self, page):
        bs = bs4.BeautifulSoup(page, 'html.parser')
        table_rows = bs.select('ul.m_pollution-list > li > a')
        links_regiones = []
        for row in table_rows:
            links_regiones.append(self.__create_link_region__(row))
        return links_regiones

    def __create_link_region__(self, row):
        linkRegion = row['href']
        region =row.span.find(text=True, recursive=False).strip()
        print ('Encontrado link para region ' + region + " " + linkRegion)
        return linkRegion

    def __get_pages_regiones(self, links_regiones):
        pages_regiones = []
        for linkRegion in links_regiones:
            pages_regiones.append(self.__get_main_page__(linkRegion, self.min_retries))
        return pages_regiones

    def crawl(self):

        print ('Cargando pagina principal')

        paginaPrincipal = self.__get_main_page__(self.url + self.subdomain, self.min_retries)
        linksRegiones = self.__parse_main_page__(paginaPrincipal)
        return self.__get_pages_regiones(linksRegiones)
