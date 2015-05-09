import os

url_file = open("urls.txt").read()
grupd_urls = url_file.split("\n\n")

urls = [a_grp for a_grp in grupd_urls]

windows=[grp.split('\n') for grp in grupd_urls]

i = 0
for tabs in windows:
	i = i + 1
	if i > 1:
		os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome")

	for url in tabs:
		if url != '':
			os.system("open -a Google\ Chrome "+url)