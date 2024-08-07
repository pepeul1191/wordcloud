from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wc(filename):
	# input data
	frecuencies = {}
	with open(filename + '.txt', 'r') as file:
		for row in file:
			word = row.strip()#.replace('-', ' ')
			if word in frecuencies:
				frecuencies[word] = frecuencies[word] + 1
			else:
				frecuencies[word] = 1
	# generate word cloud
	wordcloud = WordCloud(
		font_path='BebasNeue-Regular.ttf',
		width=800, 
		height=400, 
		background_color='white'
	).generate_from_frequencies(frecuencies)
	plt.figure(figsize=(10, 5))
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis('off')
	plt.savefig(filename + '.png', format='png')  # Save as PNG file
	plt.close()

generate_wc('metodos')
generate_wc('herramientas')
#generate_wc('metricas')
#generate_wc('roles')