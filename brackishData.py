import os
import pandas as pd
import torch
from torch.utils.data import Dataset
from skimage import io

class brackish_data(Dataset):
    label_key = {'fish':0,'small_fish':1,'crab':2,'shrimp':3,'jellyfish':4,'starfish':5}
    def __init__(self, annotations_file, images_folder, transform=None):
        cnames = ['filename', 'object_id', 'label', 'up_left_x','up_left_y','low_right_x','low_right_y']
        self.annotations = pd.read_csv(annotations_file, delimiter=';',skiprows=1,names=cnames)
        
        self.filenames = self.annotations['filename'].drop_duplicates()
        self.images_folder = images_folder
        self.transform = transform
        
        ulx, uly, lrx, lry = self.annotations['up_left_x'], self.annotations['up_left_y'], self.annotations['low_right_x'], self.annotations['low_right_y']
        self.annotations['area'] = (lrx - ulx) * (lry - uly)
        
    def __len__(self):
        return len(self.annotations)
    
    def __getitem__(self,index):
        filename = self.filenames.iloc[index]
        img_path = os.path.join(self.images_folder,filename)
        image = io.imread(img_path)
        
        annotations_filtered = self.annotations[self.annotations['filename']==filename]
        
        boxes = annotations_filtered[['up_left_x','up_left_y','low_right_x','low_right_y']]
        #might need to add torch.cuda later when cuda is enabled
        boxes = torch.FloatTensor(boxes.values.tolist())
        
        labels = annotations_filtered['label'].tolist()
        labels_int = [label_key[lbl] for lbl in labels]
        #might need to add torch.cuda later when cuda is enabled
        labels_int = torch.LongTensor(labels_int)
        
        area = torch.tensor(annotations_filtered['area'].tolist())
        
        target = {'boxes':boxes,'labels':labels_int,'image_id':filename,'area':area,'iscrowd':False}
        
        if self.transform:
            image = self.transform(image)
        
        return image, target

#this just shows an example for how to load in the data
if __name__ == '__main__':
    data_folder = '/home/ubuntu/brackishData'
    train_data = brackish_data(annotations_file=data_folder+'/annotations_AUU/train.csv', images_folder=data_folder+'images/',transform = torchvision.transforms.ToTensor())
    test_data = brackish_data(annotations_file=data_folder+'/annotations_AUU/test.csv', images_folder=data_folder+'images/',transform = torchvision.transforms.ToTensor())
    valid_data = brackish_data(annotations_file=data_folder+'/annotations_AUU/valid.csv', images_folder=data_folder+'images/',transform = torchvision.transforms.ToTensor())
 
