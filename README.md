# Infilect Assignment

### Tushar Dhyani

#### October 5, 2018


Abstract
The purpose of this project is to remove duplicates from a popular E-commerce
cdn’s little data-set dump. The provided data-set is an enormous database
containing information about the clothing products. The main aim of
this project is to remove all possible redundant data that might have
been uploaded by the respective dealers. Right now, the task is limited
to process only the sub-categorytunicsortopsfrom the given database
from which I have chosen tunics as it consisted of comparatively lesser
number of images compared to the sub-categorytop.

## 1 Introduction

After a brief research, lots and lots of googling and reading almost like 4
research papers, I came to the conclusion that the One-shot[3] learning, as
implemented in Facenet[5] and Deepface[6], should be the best approach to
tackle such a problem. This one-shot learning could be implemented by cou-
pling a pretrained model along with the Siamese network architecture and
thus provide us with a solution. This has been cited extremely well in the

## 2 Inspiration

### 2.1 Defining the problem

The dataset consisted of about 40 million images of various categories that
needed to be checked for duplicacy amongst the images. A duplicate value
could be defined as the redundant images in the dataset uploaded by the dealer.
At times this could be the same product in different sizes, but this problem
had already been solved by the productFamily column in the dataset. Which
contain the same product’s productIds there. Now the products that are same
yet does not belong to the same product family could be called as redundant or
duplicates. This could arise when the same product has been uploaded by two
different dealers or one single dealer twice.

### 2.2 The solution

Humans can solve this problem by viewing each image and comparing it with
others and neglect what may look similar but are different in sizes. Just like


humans, we will also perform checking of each and every product image with
other products that do not belong to the same product family. This could be
easily achieved by implementing what we call as One-shot learning that has been
used in Facenet[5] paper. One-shot learning could be achieved by combining
a pretrained model in such a way that it forms a network architecture that
maximizes the euclidean distance between two different images and identifies
the same images irrespective of the changes in lighting conditions and cropping
angle.

### 2.3 Siamese network

Siamese neural network is a class of neural network architectures that contain
two or more identical sub-networks. identical here means they have the same
configuration with the same parameters and weights. Parameter updating is
mirrored across both sub-networks.

### 2.4 One-shot learning

One-shot learning is an object categorization problem in computer vision. Whereas
most machine learning based object categorization algorithms require training
on hundreds or thousands of images and very large datasets, one-shot learning
aims to learn information about object categories from one, or only a few, train-
ing images.

## 3 Working - Oneshot-learning.ipynb

This notebook is the actual implementation of the codes that will carry out the
required task. It carries out the triplet loss over the inception model and gen-
erate encoding from the same. These encodings could be used to calculate the
distance between 2 images and if the distance is lesser than a specific value, the
images are similar else different. In case the two images are just the same, the
euclidean distance is 0. Thus we can match images. When these matching is cou-
pled with binary array matching, we solve our problem. I have tried to make this
notebook as descriptive as possible, and have explained each and every step that
I have taken in the notebook. But if I, in-case missed something, do it out to me.

## 4 Results

By performing the operation, we have closely detected same images. The model
perfectly works on congruent images and helps easily find all the images in the
database.

![true image1](http://img.fkcdn.com/image/tunic/3/s/c/gj19135-tu-180red-global-desi-s-200x200-imaeyzczspzxzzgx.jpeg)  ![true image2](http://img.fkcdn.com/image/tunic/3/s/c/gj19135-tu-180red-global-desi-s-200x200-imaeyzczspzxzzgx.jpeg)
```
Figure 1: The model verifies same images as True.
```
![true image](http://img.fkcdn.com/image/tunic/3/s/c/gj19135-tu-180red-global-desi-s-200x200-imaeyzczspzxzzgx.jpeg)  ![true image](http://img.fkcdn.com/image/tunic/f/y/c/gw-476-goodwill-impex-3xl-200x200-imaegtkm38vqkdyz.jpeg)
```
Figure 2: The model verifies different images as False.
```
### 4.1 Problem faced

The process used here is computationally a bit expensive and thus requires high
resources for matching. I have tried to solve the problem as far as possible under
these constraints. Even after coming up with a solution, I could not produce the
required Json file. As binary matching has time complexity ofn^2 and thus was
taking considerable time to calculate the solution. I ran my code for 2 iterations


and tried to match one single image with others and this took me 6993 seconds
to achieve this. That image had no redundancy and thus generated empty values
in Json output.

## 5 Future scope

I came across a blog on The Hacker Factor[4] which gives an idea about image
fingerprinting using pHash and dHash techniques which could be coupled with
the model further and generate the results way faster than what I am currently
getting and could thus reduce way more computational capacity than that is re-
quired right now.

## References

[1] Tzay-Yeu Wen,Large Scale Image Deduplication. Stanford University

[2] Raia Hadsell, Sumit Chopra, Yann LeCun,Dimensionality Reduction by
Learning an Invariant Mapping. The Courant Institute of Mathematical Sci-
ences, New York University

[3] Gregory Koch, Richard Zemel, Ruslan Salakhutdinov,Siamese Neural Net-
works for One-shot Image Recognition. Department of Computer Science,
University of Toronto.

[4] Neal Krawetz, Kind of Like That blog from the hacker fac-
tor. [http://www.hackerfactor.com/blog/?/archives/529-Kind-of-Like-](http://www.hackerfactor.com/blog/?/archives/529-Kind-of-Like-)
That.html, The Hacker Factor.

[5] Florian Schroff, Dmitry Kalenichenko, James Philbin,A Unified Embedding
for Face Recognition and Clustering. Google Inc.

[6] Yaniv Taigman Ming Yang, Marc’Aurelio Ranzato, Lior Wolf,Closing the
Gap to Human-Level Performance in Face Verification. Facebook AI Re-
search.