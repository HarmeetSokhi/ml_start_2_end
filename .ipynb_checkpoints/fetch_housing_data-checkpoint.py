{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import tarfile\n",
    "import urllib\n",
    "\n",
    "DOWNLOAD_ROOT = \"https://raw.githubusercontent.com/ageron/handson-ml2/master/\"\n",
    "HOUSING_PATH = os.path.join(\"datasets\",\"housing\")\n",
    "HOUSING_URL =  DOWNLOAD_ROOT + \"datasets/housing/housing.tgz\"\n",
    "\n",
    "def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):\n",
    "    os.makedirs(housing_path, exist_ok=True)\n",
    "    tgz_path = os.path.join(housing_path,\"housing.tgz\")\n",
    "    urllib.request.urlretrieve(housing_url, tgz_path)\n",
    "    housing_tgz=tarfile.open(tgz_path)\n",
    "    housing_tgz.extractall(path=housing_path)\n",
    "    housing_tgz.close()\n",
    "    \n",
    "fetch_housing_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def load_housing_data(housing_path=HOUSING_PATH):\n",
    "    csvpath"
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
