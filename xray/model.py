import torch
import torchvision
from torchvision import transforms
import PIL
import io
import torch.nn as nn
device = torch.device('cpu')
#'cuda:0' if torch.cuda.is_available() else
TheModelClass = torchvision.models.resnet152(pretrained=True)


from collections import OrderedDict

new_fc = nn.Sequential(OrderedDict([
                          ('fc1', nn.Linear(2048, 1024)),
                          ('relu', nn.ReLU()),
                          ('fc2', nn.Linear(1024, 2)),
                          ('output', nn.LogSoftmax(dim=1))
                          ]))

for param in TheModelClass.parameters():
  param.requires_grad = False
#
TheModelClass.fc = new_fc
TheModelClass = TheModelClass.to(device)


model = TheModelClass
# TODO: fix path 
model.load_state_dict(torch.load("/home/usernamemeow/HMD/xray/model.pth", map_location='cpu'))
model.eval()
model = model.to(device)


transform = transforms.Compose([ transforms.Resize((224,224)),
                #transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])


def open_image(img_path):
    #image = PIL.Image.open(img_path).convert('RGB')
    image = PIL.Image.open(io.BytesIO(img_path)).convert('RGB')
    image = transform(image).unsqueeze(0)
    image = image.to(device)
    outputt = model(image)
    _, va_pred1 = torch.max(outputt, 1)
    return va_pred1.item()

