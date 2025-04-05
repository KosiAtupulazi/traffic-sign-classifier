# traffic-sign-classifier

1. Author: Kosi Atupulazi
2. Purpose: Learning ML Fundamentals
3. Dataset: LISA Traffic Signs Dataset (Kaggle)

## 📁 Dataset Setup
### Option 1: Manual Download


This project uses the [LISA Traffic Light Dataset](https://www.kaggle.com/datasets/mbornoe/lisa-traffic-light-dataset).

Due to size limitations, the dataset is not included in this repo but I have included **lisa_sample** for prototyping.

To set it up:

1. Download the dataset manually from [Kaggle](https://www.kaggle.com/datasets/mbornoe/lisa-traffic-light-dataset)
2. Unzip it into a folder named `lisa_dataset/` in the root of this project.

### Option 2: Terminal Download (Kaggle CLI)

#### 1. Set up your Kaggle API key

- Go to: [https://www.kaggle.com/account](https://www.kaggle.com/account)
- Scroll to the **API** section and click **"Create New API Token"**
- This downloads a file called `kaggle.json`
- Move it to the correct location:
  ```bash
  mkdir -p ~/.kaggle
  mv /path/to/kaggle.json ~/.kaggle/
  chmod 600 ~/.kaggle/kaggle.json

#### 2. Install the Kaggle CLI
  ```bash
    pip install kaggle
    kaggle datasets download -d mbornoe/lisa-traffic-light-dataset
    unzip lisa-traffic-light-dataset.zip -d lisa_dataset
```
#### 3. Project Setup
```bash
    python -m venv trafficenv
    source trafficenv/bin/activate
    pip install -r requirements.txt
    jupyter notebook traffic_sign.ipynb
```
