import pandas as pd
from torch.utils.data import Dataset, DataLoader
import torch

# 自定义数据集类
class MyDataset(Dataset):
    def __init__(self, file):
        # 读取 CSV 文件并预处理
        self.data = pd.read_csv(file)
        # 将特征和标签分开
        self.features = self.data[['feature1', 'feature2', 'feature3']].values
        self.labels = self.data['labels'].values

    def __getitem__(self, index):
        # 获取指定索引处的特征和标签
        feature = self.features[index]
        label = self.labels[index]
        # 转换为 PyTorch 张量
        feature = torch.tensor(feature, dtype=torch.float32)
        label = torch.tensor(label, dtype=torch.long)
        return feature, label

    def __len__(self):
        # 返回数据集的大小
        return len(self.data)

# 创建数据集对象
dataset = MyDataset(r'C:\Users\wsb\Desktop\Gitdemo\Python-test\Dataset\data3.csv')

# 使用 DataLoader 加载数据
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# 迭代 DataLoader 以查看加载的数据
for batch in dataloader:
    features, labels = batch
    print(f"Features: {features}, Labels: {labels}")
