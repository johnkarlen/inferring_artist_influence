# inferring_artist_influence

This project contains code for scraping images of famous fine art from http://www.artchive.com/, and then using transfer learning to learn properties of individual artists. I retrieved 50 images per artist.

- scrape_art_imgaes.py pulls the images from the artchive
- art_tf_script.sh will run tensorflow. It closely follows a tutorial found here: https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0
- find_similar_imgs.py compares bottlenecks to find the most similar image to each image in an artists portfolio of the set of all other possible images (every other artists portfolio). 
- montage_pairs.sh and montage_pairs_vert.sh combine the similar images into pdfs using the imagemagick library

