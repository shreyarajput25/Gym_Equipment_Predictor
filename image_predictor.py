import torch    #Pytorch
import os
import torchvision.transforms as tt #To apply transformations to the dataset, augmenting it and transforming it to a tensor.
from torchvision import transforms
from torch.autograd import Variable

to_pil = transforms.ToPILImage()

device = torch.device("cpu")
model_dir = 'model/equipment_classfication_model.pth'
model=torch.load(model_dir, map_location ='cpu')
model.eval()
print('model loaded')

test_transforms = transforms.Compose([transforms.Resize(size=(224,224)),
                                      transforms.ToTensor(),
                                     ])

def predict_image(image):
  image_tensor = test_transforms(image).float()
  image_tensor = image_tensor.unsqueeze_(0)
  input = Variable(image_tensor)
  input = input.to(device)
  output = model(input)
  index = output.data.cpu().numpy().argmax()
  return index