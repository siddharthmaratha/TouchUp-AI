import torch
import open_clip
from torchvision import transforms
from torchvision.transforms import ToPILImage
import torch.nn.functional as F




class help_function:
    def __init__(self):
        self.clip_text_model = torch.jit.load('jit_models/clip_text_jit.pt', map_location=torch.device('cpu'))
        self.decoder = torch.jit.load('jit_models/decoder_16w.pt', map_location=torch.device('cpu'))
        self.mapper_clip = torch.jit.load('jit_models/mapper_clip_jit.pt', map_location=torch.device('cpu'))
        self.mean_clip = torch.load('jit_models/mean_clip.pt')
        self.mean_person = torch.load('jit_models/mean_person.pt')
        self.encoder = torch.jit.load('jit_models/combined_encoder.pt', map_location=torch.device('cpu'))
        self.tokenizer = open_clip.get_tokenizer('ViT-B-32')
        self.transform = transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])

    def get_text_embedding(self, text):
        text = self.clip_text_model(self.tokenizer(text))
        return text

    def get_image_inversion(self, image):
        image = self.transform(image)
        if not image.shape == torch.Size([3, 224, 224]):
            image = image.reshape(1,3,image.shape[1],image.shape[2])
            image = F.interpolate(image, [224,224], mode='bilinear', align_corners=True)

        w_inversion = self.encoder(image.reshape(1,3,224,224)).reshape(1,16,512)
        return w_inversion + self.mean_person

    def get_text_delta(self,text_feachers):
        w_delta = self.mapper_clip(text_feachers - self.mean_clip)
        return w_delta


    def image_from_text(self,text,image,power = 1.0):
        w_inversion = self.get_image_inversion(image)
        if power != 0:
            text_embedding = self.get_text_embedding(text)
            w_delta = self.get_text_delta(text_embedding)
            w_edit = w_inversion + w_delta * power
        else:
            w_edit = w_inversion
        image_edit = self.decoder(w_edit)
        image_edit = ToPILImage()((image_edit[0]+0.5)*0.5).resize((512,512))
        return image_edit
