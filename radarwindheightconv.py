import argparse, sys

def getsfcwind(height, wind):
	import pickle
	with open('heightconvseries.pickle','rb') as f:
		series = pickle.load(f)
	targetheight = round(height,-1)
	#print(series[series.index == 0].values)
	return (wind/series[series.index == targetheight].values)*series[series.index == 0].values

if __name__ == "__main__":
	# Parse arguments!!
	parser = argparse.ArgumentParser(
	                    prog='radarwindheightconv.py',
	                    description='Gets an expected surface wind from a height (m) and radar wind (kt)',
	                    epilog='')
	parser.add_argument('height')
	parser.add_argument('wind')
	args = parser.parse_args(sys.argv[1:])
	print(getsfcwind(float(args.height), float(args.wind)))