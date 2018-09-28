import numpy as np
import glob
import sys
from sklearn.decomposition import PCA

homer_path = "tensorflow-for-poets-2/tf_files/bottlenecks/homer"
homer_bnecks = glob.glob(homer_path + "/*")

other_painters = glob.glob("tensorflow-for-poets-2/tf_files/bottlenecks/*")
if homer_path in other_painters: other_painters.remove(homer_path)

other_paintings = []
painting_list = []
painter_names = []
painting_names = []

for op in other_painters:
    painters_dir = glob.glob(op + "/*")
    painting_list = painting_list + painters_dir
    next_paintings = [np.genfromtxt(hp, delimiter=',') for hp in painters_dir]
    painter_names = painter_names + [op.split("/")[-1] + ": " + hp.split("/")[-1].split(".")[0] for hp in painters_dir]
    painting_names = painter_names + [op.split("/")[-1] for hp in painters_dir]
    other_paintings = other_paintings + next_paintings

painting_names = painting_names + ["homer" + ": " + i.split("/")[-1].split(".")[0] for i in homer_bnecks]
painter_names = painter_names + ["homer" + ": " + i.split("/")[-1].split(".")[0] for i in homer_bnecks]

homer_paintings = [np.genfromtxt(hp, delimiter=',') for hp in homer_bnecks]
other_paintings = np.array(other_paintings)

for idx in range(len(homer_paintings)):
    similarities = np.einsum('j, ij->i', homer_paintings[idx], other_paintings)
    print("montage -geometry +2+2 \\")
    [hpth,hlbl,tl] = homer_bnecks[idx].partition(".jpg")
    homer_jpg = "imgs/" + hpth.split("/")[-2] + "/" + hpth.split("/")[-1] + ".jpg"
    print(homer_jpg + " \\")
    [pth,lbl,tl] = painting_list[np.argmax(similarities)].partition(".jpg")
    other_jpg = "imgs/" + pth.split("/")[-2] + "/" + pth.split("/")[-1] + ".jpg"
    print(other_jpg + " \\")
    print("outpairs/" + hpth.split("/")[-1] + "pair" + ".jpg")

print(other_paintings.shape)
X = np.vstack((other_paintings, np.array(homer_paintings)))

pca = PCA(n_components=2)
t_X = pca.fit_transform(X)

np.save("t_X.npy", t_X)

labels = open('labels.txt', 'w')
for item in painter_names:
  labels.write("%s\n" % item)
labels.close()

labels = open('painters.txt', 'w')
for item in painting_names:
  labels.write("%s\n" % item)
labels.close()
