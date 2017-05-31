from lxml.html import parse
from urllib.request import urlopen, quote
import os

def download_and_save(url):
	filename = url.split('/')[-1]
	if not os.path.isfile('data/' + filename):
		url = '/'.join(url.split('/')[:-1]) + '/' + quote(filename)
		if url:
			pauta = urlopen(url)
			with open('data/'+filename, 'b+w') as f:
				f.write(pauta.read())

pauta_url = "http://www.camara.sp.gov.br/atividade-legislativa/sessao-plenaria/pauta-das-sessoes/"

soup = parse(pauta_url).getroot()

for p in soup.xpath("//ul[@class='box-downloads-list']/li/a"):
	try:
		download_and_save(p.get('href'))
	except:
		print("Could not download " + p.get('href'))