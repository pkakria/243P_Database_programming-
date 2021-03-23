import re, sys, collections, glob, concurrent.futures

def count_text(filepath):
	print("Counting " + filepath)
	words = re.findall('\w{3,}', open(filepath).read().lower())
	counts = collections.Counter(w for w in words if w not in stopwords)
	print("Done counting " + filepath)
	return counts

stopwords = set(open('stop_words').read().split(','))
files = glob.glob('*.txt')
aggregated = collections.Counter()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
	futures = [executor.submit(count_text, file) for file in files]
	for future in concurrent.futures.as_completed(futures):
		try:
			counts = future.result()
			aggregated += counts
		except Exception as exc:
			print(exc)

#Print out aggregated most  common
for (w, c) in aggregated.most_common(25):
    print(w, '-', c)