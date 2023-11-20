import json

with open('/home/winch/0x590/web/Babymetal-fan-site/songs/template.html', 'r') as file:
	template = file.read()

with open('/home/winch/0x590/web/Babymetal-fan-site/songs.json', 'r') as file:
	data = json.load(file)
	
	for entry in data:
		result = template.replace('SONG', entry['song'])

		if 'text' in entry:
			text = entry['text']

			if isinstance(text, str):
				result = result.replace('TEXT', text)
			elif isinstance(text, list):
				htmlCode = ''
				for txt in text:
					htmlCode += txt if txt.startswith('<') else '<p>' + txt + '<p>'
				
				result = result.replace('TEXT', htmlCode)
		else:
			result = result.replace('TEXT', '<p>Ещё не сделано :(</p>')
		

		links = entry['links']

		if len(links) > 0:
			result = result.replace('LINKS', '<h2>Ссылки</h2>\n\t\t\t<ul>\n\t\t\t\t' + '\n\t\t\t\t'.join(f'<li><a href="{link["href"]}">{link["name"]}</a></li>' for link in links) + '\n\t\t\t</ul>')
		else:
			result = result.replace('LINKS', '')
		
		with open('/home/winch/0x590/web/Babymetal-fan-site/songs/' + entry['file'], 'w') as html:
			html.write(result)