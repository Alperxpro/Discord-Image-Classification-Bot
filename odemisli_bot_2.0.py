import discord
from discord.ext import commands
import requests
import os
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

IMAGE_DIR="images"
os.makedirs(IMAGE_DIR,exist_ok=True)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def messi(ctx):
    with open('Gonderilen_gorseller/messi.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)
        
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def FB_deki_en_iyi_futbolcu(ctx):
    await ctx.send("Edin Dzeko")
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command()
async def cevre_kirliligi_ile_fikra_anlat(ctx):
    fikra = "Bir gün Nasrettin Hoca, köydeki çeşmenin başında oturmuş düşünüyormuş. Köylülerden biri gelmiş ve demiş ki: Hoca, bu çevre kirliliği çok arttı. Ne yapacağız?Nasrettin Hoca gülümseyerek cevap vermiş:Kolay, her yere bir tabela koyarız: 'Çöp Atmak Yasaktır!' Köylü şaşırarak sormuş:Hoca, o kadar tabela asmak çözüm olur mu?Hoca yine gülümseyerek cevaplamış:Tabelaya bakanlar o kadar meşgul olur ki çöp atmayı unutur!"
    await ctx.send(fikra)
@bot.command()
async def analiz_et(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = os.path.join(IMAGE_DIR,file_name)
            try:
                await attachment.save(file_path)
                class_name,confidence_score = get_class(file_path)
                await ctx.send("Görseli kaydettim")
                await ctx.send(f"Bu kuş yüzde {confidence_score} {class_name}.")
                if class_name == "Kanarya":
                    await ctx.send("Bu bir kanarya. Evde beslemek için ideal. Yem, buğday vb. tahıllarla besleyebilirsin")
                elif class_name == "Guvercin":
                    await ctx.send("Bu bir güvercin. Yem,buğday vb. tahıllarla besleyebilirsin")
                elif class_name == "Serce":
                    await ctx.send("Bu bir serçe. Yem, buğday vb. tahıllarla beslenebilir.")
                elif class_name == "Baykus":
                    await ctx.send("Bu bir baykuş. Kendi yemeğini kendisi bulabilir.")
                elif class_name == ("Kumru"):
                    await ctx.send("Bu bir kumru. Yem, buğday vb. tahıllarla beslenebilir.")
                elif class_name == "Sinekkusu":
                    await ctx.send("Bu bir sinek kuşu. Kendi yemeğini kendisi bulabilir.")
                elif class_name == "Leylek":
                    await ctx.send("Bu bir leylek. Kendi yemeğini kendisi bulabilir")

            except Exception as e:
                await ctx.send(f"Şu anda bunu yapamıyorum{e}")
    else:
        await ctx.send("Neden beni yordun? Niye görsel göndermedin?")
    






bot.run("TOKEN HERE")
