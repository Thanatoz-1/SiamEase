Introduction {#sec:introduction}
============

After a brief research, lots and lots of googling and reading almost like 4 research papers, I came to the conclusion that the One-shot@siamese learning, as implemented in [Facenet@facenet](https://arxiv.org/pdf/1503.03832.pdf) and [Deepface@deepface](https://research.fb.com/wp-content/uploads/2016/11/deepface-closing-the-gap-to-human-level-performance-in-face-verification.pdf), should be the best approach to tackle such a problem. This one-shot learning could be implemented by coupling a pretrained model along with the Siamese network architecture and thus provide us with a solution. This has been cited extremely well in the

Inspiration {#sec:theory}
===========

Defining the problem
--------------------

The dataset consisted of about 40 million images of various categories that needed to be checked for duplicacy amongst the images. A duplicate value could be defined as the redundant images in the dataset uploaded by the dealer. At times this could be the same product in different sizes, but this problem had already been solved by the productFamily column in the dataset. Which contain the same product’s productIds there. Now the products that are same yet does not belong to the same product family could be called as redundant or duplicates. This could arise when the same product has been uploaded by two different dealers or one single dealer twice.

The solution
------------

Humans can solve this problem by viewing each image and comparing it with others and neglect what may look similar but are different in sizes. Just like humans, we will also perform checking of each and every product image with other products that do not belong to the same product family. This could be easily achieved by implementing what we call as One-shot learning that has been used in Facenet@facenet paper. One-shot learning could be achieved by combining a pretrained model in such a way that it forms a network architecture that maximizes the euclidean distance between two different images and identifies the same images irrespective of the changes in lighting conditions and cropping angle.

Siamese network
---------------

Siamese neural network is a class of neural network architectures that contain two or more identical sub-networks. identical here means they have the same configuration with the same parameters and weights. Parameter updating is mirrored across both sub-networks.

One-shot learning
-----------------

One-shot learning is an object categorization problem in computer vision. Whereas most machine learning based object categorization algorithms require training on hundreds or thousands of images and very large datasets, one-shot learning aims to learn information about object categories from one, or only a few, training images.

Working
=======

The project has been divided into two sub-categories for simplifying the solution and reduce the computational resources that would be required during pipelining the complete problem-set.

Oneshot-learning.ipynb
----------------------

This notebook is the actual implementation of the codes that will carry out the required task. It carries out the triplet loss over the inception model and generate encoding from the same. These encodings could be used to calculate the distance between 2 images and if the distance is lesser than a specific value, the images are similar else different. In case the two images are just the same, the euclidean distance is 0. Thus we can match images. When these matching is coupled with binary array matching, we solve our problem. I have tried to make this notebook as descriptive as possible, and have explained each and every step that I have taken in the notebook. But if I, in-case missed something, do it out to me.

Results
=======

By performing the operation, we have closely detected same images. The model perfectly works on congruent images and helps easily find all the images in the database.

![[fig:result]The model verifies different images as *False*.](1.png){width="100.00000%"}

![[fig:result]The model verifies different images as *False*.](2.png){width="100.00000%"}

Problem faced
-------------

The process used here is computationally a bit expensive and thus requires high resources for matching. I have tried to solve the problem as far as possible under these constraints. Even after coming up with a solution, I could not produce the required Json file. As binary matching has time complexity of $n^{2}$ and thus was taking considerable time to calculate the solution. I ran my code for 2 iterations and tried to match one single image with others and this took me 6993 seconds to achieve this. That image had no redundancy and thus generated empty values in Json output.

Future scope
============

I came across a blog on The Hacker Factor@thf which gives an idea about image fingerprinting using pHash and dHash techniques which could be coupled with the model further and generate the results way faster than what I am currently getting and could thus reduce way more computational capacity than that is required right now.

<span>9</span> Tzay-Yeu Wen, *Large Scale Image Deduplication*. Stanford University Raia Hadsell, Sumit Chopra, Yann LeCun, *Dimensionality Reduction by Learning an Invariant Mapping*. The Courant Institute of Mathematical Sciences, New York University Gregory Koch, Richard Zemel, Ruslan Salakhutdinov, *Siamese Neural Networks for One-shot Image Recognition*. Department of Computer Science, University of Toronto. Neal Krawetz, *Kind of Like That blog from the hacker factor*. http://www.hackerfactor.com/blog/?/archives/529-Kind-of-Like-That.html, The Hacker Factor. Florian Schroff, Dmitry Kalenichenko, James Philbin, *A Unified Embedding for Face Recognition and Clustering*. Google Inc. Yaniv Taigman Ming Yang, Marc’Aurelio Ranzato, Lior Wolf, *Closing the Gap to Human-Level Performance in Face Verification*. Facebook AI Research.
