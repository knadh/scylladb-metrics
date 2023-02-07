#!/bin/python3

from datetime import datetime
import sys
import urllib.request

def generate(metrics_url: str):
	if metrics_url.startswith("http:"):
		with urllib.request.urlopen(metrics_url) as r:
			data = r.read().decode("utf-8")
	else:
		with open(metrics_url) as r:
			data = r.read()

	rows = []
	n = 0
	for l in data.splitlines():
		if l.startswith("# HELP"):
			parts = l.split(" ")
			name = parts[2]
			desc = " ".join(parts[3:])

		if l.startswith("# TYPE"):
			typ = l.split(" ")[3]
			n += 1

			rows.append("""
				<tr>
				<td>{}</td>
				<td class="metric">{}</td>
				<td>{}</td>
				<td>{}</td>
				</tr>
			""".format(n, name, typ, desc))

	# Read the HTML template and fill content.
	with open("template.html", "r") as f:
		tpl = f.read()

	tpl = tpl.replace("$rows", "\n".join(rows)).replace("$date", datetime.now().strftime("%Y-%m-%d"))

	print(tpl)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: {} $file_or_scylla_url > index.html".format(sys.argv[0]))
		print("Example: {} ./metrics > index.html".format(sys.argv[0]))
		print("Example: {} http://scylla-url:9180/metrics > index.html".format(sys.argv[0]))
		sys.exit(1)

	generate(sys.argv[1])
