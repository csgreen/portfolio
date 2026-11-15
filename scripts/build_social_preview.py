from PIL import Image, ImageDraw, ImageFont
import base64, io, re, os
from pathlib import Path
svg=Path('assets/christina-portrait-hq.svg').read_text()
encoded=re.search(r'data:image/webp;base64,([^"]+)',svg).group(1)
portrait=Image.open(io.BytesIO(base64.b64decode(encoded))).convert('RGB')
w,h=1200,630
im=Image.new('RGB',(w,h),'#fffaf6')
d=ImageDraw.Draw(im)
navy='#14213d'; coral='#ed705b'; muted='#526075'
serif='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
sans='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def f(path,size): return ImageFont.truetype(path,size)
d.text((76,65),'Christina Green',font=f(serif,45),fill=navy)
d.ellipse((407,98,418,109),fill=coral)
d.text((76,198),'I build products',font=f(serif,54),fill=navy)
d.text((76,276),'people have to trust.',font=f(serif,47),fill=navy)
d.line((76,352,186,352),fill=coral,width=6)
d.text((76,401),'PRODUCT LEADERSHIP',font=f(sans,21),fill=muted)
d.text((76,444),'Security  /  Identity  /  AI',font=f(sans,21),fill=navy)
d.text((76,555),'csgreen.github.io/portfolio',font=f(sans,17),fill=muted)
portrait=portrait.resize((342,428))
im.paste(portrait,(802,113))
d.rectangle((800,111,1145,542),outline='#e8e3df',width=3)
Path('assets/social-preview.png').parent.mkdir(parents=True,exist_ok=True)
im.save('assets/social-preview.png',optimize=True)
