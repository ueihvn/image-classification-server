# [Prod] Predict 1 image
import torch
from PIL import Image
from urllib.request import urlopen
from torchvision import transforms
import operator
import json

# ================ INIT ================

MIN_PRIMARY_GENRE_PERCENT = 50
MIN_GENRE_PERCENT = 20
MAX_RETURN_GENRE = 3

genres=["Children", 'Comics', 'Computer', 'Cooking', 'History', 'Parenting', 'Romance', 'Science Fiction', 'Test Preparation', 'Travel']

img_url = 'https://blog-cdn.reedsy.com/uploads/2019/12/stargazing-705x1024.jpg'

# final output
predict_genres = [] 

#  load model 
MODEL_PATH = 'model/model_v3.pt'
device = torch.device("cpu")
resnet_model = torch.load(MODEL_PATH, map_location=torch.device(device))
resnet_model.eval()

#  init method to resize img
preprocess = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

# ================ MAIN ================

#  load & preprocessing image
input_img = Image.open( urlopen(img_url) ).convert('RGB')
preprocess_input_img = preprocess(input_img)
unsqueeze_input_img = torch.unsqueeze(preprocess_input_img, 0)

# predict 
output = resnet_model(unsqueeze_input_img)
percentages = torch.nn.functional.softmax(output, dim=1)[0] * 100

has_primary_genre = False

# map genre with percent
for index, item in enumerate(percentages):
    percent = percentages[index].item()
    genre_name = genres[index]

    # use for removing low-percent genre if already has high one (above 50)
    if percent >= MIN_PRIMARY_GENRE_PERCENT:
        has_primary_genre = True

    predict_genres.append({ 
            'genre': genre_name, 
            'percent': percent
        })
# print( 'All genre percent: \t', json.dumps(predict_genres, sort_keys=True, indent=4), '\n\n')

# get top 3 highest percent
predict_genres.sort(key=operator.itemgetter('percent'), reverse=True)
predict_genres = predict_genres[0:MAX_RETURN_GENRE]
print( 'Top 3: ', json.dumps(predict_genres, sort_keys=True, indent=4), '\n\n')

# filter genres above x % if has primary genre
if has_primary_genre:
    predict_genres = [ item for item in predict_genres if item['percent'] >= MIN_GENRE_PERCENT ]
print( 'Filter: ', json.dumps(predict_genres, sort_keys=True, indent=4), '\n\n')

# list of dict -> array
predict_genres = [ item['genre'] for item in predict_genres ]
print('Final output: ', predict_genres)

def PredictGenres(coverImagesLink):
	predict_genres = [] 
	input_img = Image.open( urlopen(img_url) ).convert('RGB')
	preprocess_input_img = preprocess(input_img)
	unsqueeze_input_img = torch.unsqueeze(preprocess_input_img, 0)

	# predict 
	output = resnet_model(unsqueeze_input_img)
	percentages = torch.nn.functional.softmax(output, dim=1)[0] * 100
	for index, item in enumerate(percentages):
		percent = percentages[index].item()
		genre_name = genres[index]
	    # use for removing low-percent genre if already has high one (above 50)
		if percent >= MIN_PRIMARY_GENRE_PERCENT:
			has_primary_genre = True
		predict_genres.append({ 
	            'genre': genre_name, 
	            'percent': percent
	        })
	return predict_genres
