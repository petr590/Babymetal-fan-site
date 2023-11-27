import os

SITE = '/home/winch/0x590/web/Babymetal-fan-site/'
PHOTO = SITE + 'photo/'

with open(PHOTO + 'template.html', 'r') as file: template = file.read()
with open(PHOTO + 'index-template.html', 'r') as file: index_template = file.read()


def create_dir(dir: str, filename: str) -> str:
	os.makedirs(dir, exist_ok=True)
	return os.path.join(dir, filename)

def escape(s: str) -> str:
	return s.replace('\\', '\\\\').replace('"', '\\"').replace('$', '\\$')


def generate_file(dirname: str, member_name: str, member_full_name: str) -> None:
	dir = '/home/winch/0x590/BM/Imgs/' + dirname
	result_dir_name = member_name.lower()

	links = []

	for subdir_name in os.listdir(dir):
		subdir = os.path.join(dir, subdir_name)
		if os.path.isdir(subdir):
			images = []

			for image_file_name in filter(lambda file: file.endswith('.jpg') or file.endswith('.png'), os.listdir(subdir)):
				image = os.path.join(subdir, image_file_name)

				if os.path.isfile(image):
					target = create_dir(f'{SITE}/imgs/photo/{result_dir_name}/{subdir_name}', image_file_name)

					if not os.path.exists(target):
						os.system(f'ln "{escape(image)}" "{escape(target)}"')

					images.append(f'<img class="photo" src="imgs/photo/{result_dir_name}/{subdir_name}/{image_file_name}">')

			if len(images) > 0:
				links.append(f'<a href="photo/{result_dir_name}/{subdir_name}.html">{subdir_name}</a>')

				with open(create_dir(PHOTO + result_dir_name, subdir_name + '.html'), 'w') as file:
					content = template.replace('FULLNAME', member_full_name).replace('PATHNAME', result_dir_name).replace('NAME', member_name)
					content = content.replace('SUBDIR', subdir_name).replace('IMAGES', '\n\t\t\t\t'.join(images))
					file.write(content)


	with open(create_dir(PHOTO + result_dir_name, 'index.html'), 'w') as file:
		content = index_template.replace('FULLNAME', member_full_name).replace('NAME', member_name)
		content = content.replace('LINKS', '<br>\n\t\t\t\t'.join(links))
		file.write(content)


generate_file('Su-Metal', 'Su-metal', 'Судзука Накамото')
generate_file('Moa-Metal', 'Moa-metal', 'Моа Кикучи')
generate_file('Yui-Metal', 'Yui-metal', 'Юи Мидзуно')
generate_file('Momo-Metal', 'Momo-metal', 'Момоко Окадзаки')
generate_file('BabyMetal', 'Babymetal', 'Babymetal')