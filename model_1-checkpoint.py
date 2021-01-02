{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "train_path = r\"C:\\Users\\Toshiba\\Desktop\\CNN MODEL\\train_2\"\n",
    "val_path = \"\"\n",
    "test_path = \"\"\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(151, 448, 448, 4)"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os \n",
    "import cv2\n",
    "import numpy as np\n",
    "from skimage import io\n",
    "import matplotlib.pyplot as plt \n",
    "imege = []\n",
    "os.chdir(train_path)\n",
    "for img_path in os.listdir(train_path):\n",
    "    imgs = plt.imread(img_path)\n",
    "    imege.append(imgs)\n",
    "X = np.array(imege,dtype='float32')\n",
    "X.shape\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
