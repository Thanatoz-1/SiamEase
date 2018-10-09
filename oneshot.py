import os
import keras
import cv2
from urllib.request import urlretrieve
from tqdm import tqdm
import pandas as pd 
import numpy as np
import json

def triplet_loss(y_true, y_pred, alpha = 0.2):
	'''
	Returns the triplet loss.
	'''
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    pos_dist = tf.reduce_sum(tf.square(anchor - positive))
    neg_dist = tf.reduce_sum(tf.square(anchor - negative))
    basic_loss = pos_dist - neg_dist + alpha
    loss = tf.maximum(basic_loss, 0)    
    return loss


def init_model(input_shape=(200,200,3)):
	'''
	Initalizes the model and returns the model

	Arguments:
	input_shape: shape of image input along with channels
	Default is (200,200,3) and if you wish to change, it should be greater than this.
	'''
	assert(input_shape[0]<200 or input_shape[1]<200), 'Shape cannot be less than 200'
	assert(input_shape[2]!=3), 'RGB channels required'
	RecModel = InceptionV3(input_shape=input_shape, weights=None, include_top=False)
	RecModel.compile(optimizer='adam', loss = triplet_loss, metrics = ['accuracy'])
	return RecModel

#Image encoding. The main aim of this function is to convert the images to encodings.
def image_to_encoding(image_name, model):
	'''
	Images to encoding runs one forward propogation on the image and creates encodings.

	Arguments:
	image_name: Image name is the name of image to encode with extension
	model: The model on which we have to forward propogate
	'''

    #Read the image and convert BGR to RGB
    a = cv2.imread('./images/'+str(image_name),cv2.COLOR_BGR2RGB)
    #Generate the image padding using np.zeros
    b = np.zeros((200,200,3), dtype='uint8')
    #Add the slice of image over the padding
    b[:a.shape[0],:a.shape[1],:]+=a
    #Convert to batch
    b = b.reshape(1,200,200,3)
    #Forward propagate through the model network
    embedding = model.predict_on_batch(b)
    return embedding

def create_encodings(path_to_images='./images'):
	'''
	This generates embeddings and take 0.15s for each element of dataset
	So use accordingly.

	Arguments:
	path_to_image = pass the path to image string to the function.
	'''
	imgs = os.listdir('./images')
	database={}
	for i,img in enumerate(sorted(imgs)):
	    database[img.split('.')[0]]=image_to_encoding(img, RecModel)
    return database

#Function to verify the images with the identity
def verify(image,identity, database, model):
    """
    Function that verifies Redundant images
    
    Arguments:
    image_path -- path to an image
    identity -- string, productId you'd like to verify the identity.
    database -- python dictionary mapping Products to their encodings (vectors).
    model -- your ResNet model instance in Keras
    
    Returns:
    dist -- distance between the image_path and the image of "identity" in the database.
    same -- True, if the images are same. False otherwise.
    """
    
    # Step 1: Compute the encoding for the image. Use image_to_encoding()
    encoding = image_to_encoding(image, model)
    # Step 2: Compute distance with identity's image (≈ 1 line)
    dist = np.linalg.norm(database[identity] - encoding)
    
    # Step 3: Open the door if dist < 0.7, else don't open (≈ 3 lines)
    if dist < 1:
        same = True
    else:
        same = False
    return dist, same

if __name__ == '__main__':
	if not os.path.exists('./dataset'):
		os.mkdir('./dataset')
	if not os.path.exists('./images/'):
		try:
			link_zip='https://transfer.sh/ShBts/images_fkcdn.zip'
			link_tunics='https://transfer.sh/8gQj4/tunics.csv'
			if os.path.exists('./dataset/images_fkcdn.zip'):
				os.system('unzip ./dataset/images_fkcdn.zip')
			else:
				urlretrieve(link_zip,'./dataset/images_fkcdn.zip')
				urlretrieve(link_tunics,'./dataset/tunics.csv')
		except Exception as e:
			print(e)

	RecModel=init_model()
	database=create_encodings()
	df = pd.read_csv('tunics.csv')
	productFamily=json.load(open('pf.json'))
	imgs=sorted(os.listdir('./images'))
	#Compare each image with all other image in array
	checks={}
	ptr=0

	# This loops compares the image with the preceeding images and 
	# not with the already visited images to overcome redundancy
	for i in range(2):
	    anchor_image=imgs[i]
	    anchor_name=imgs[i].split('.')[0]
	    checks[anchor_name]=[]
	    for j in range(i+1,len(imgs)):
	        target_image=imgs[j]
	        target_name=imgs[j].split('.')[0]
	        if target_name not in productFamily[anchor_name] and verify(anchor_image, target_name, database, RecModel)[1] :
	            checks[anchor_name].append(target_name)
	            print(ptr)
	            ptr+=1

    # Dump the json to the temp server
    import json
    with open('output.json','w') as f:
        json.dump(checks,f)
