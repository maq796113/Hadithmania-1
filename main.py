import discord
from discord.ext import commands
import os

from keep_it_running import keep_running
import requests



bot = commands.Bot(command_prefix = '&')

def get_hadith(ref_):

  _ref = ref_.split()
  
  a = _ref[0]

  b = int(_ref[1].split(":")[0])

  


  c = int(_ref[1].split(":")[1])
  
 
 
  
    
  c=c-1




  j=0
  payload = {'content-type': "application/json"}
  headers = {
      'x-api-key': "SqD712P3E82xnwOAEOkGd5JZH8s9wRR24TqNFzjk"
      }
  r = requests.get( f"https://api.sunnah.com/v1/collections/{a}/books/{b}/hadiths", params=payload, headers=headers)
  res=r.json()
  
  for i in res['data']:

    if j==c:
      
      hadith_pt2 = i["hadith"][0]["body"]
      hadith_pt2= hadith_pt2.replace("<p>", "")
      hadith_pt2 = hadith_pt2.replace("</p>",'')
      hadith_pt3 = i["hadith"][0]["grades"][0]['grade']
      hadith_pt5 = i["hadith"][1]["body"]
      hadith_pt5 = hadith_pt5.replace("<p>", "")
      hadith_pt5 = hadith_pt5.replace("</p>",'')
      
      hadith_num = i["hadithNumber"]
      return hadith_pt5,hadith_pt2,hadith_pt3, hadith_num
      
      


    else:

      j+=1
    
    
    
    
   
    
    



@bot.command(aliases = ['h'])
async def hadith(ctx, *,ref_):

  re = ref_.split()
  arabic, english, hukm, hnum = get_hadith(ref_)
  hnum = hnum.split()
 
  if re[0] == "bukhari" or re[0] == "muslim":
    string = "Sahih"
  embed=discord.Embed(
    title=f"{string} {re[0].capitalize()} {hnum[0]}{hnum[1]}",
    url=f"https://sunnah.com/{re[0]}:{hnum[0]}{hnum[1]}",
    description= "Here is your requested hadith",
    color=discord.Color.green())
    
    
  embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Hadith1.png")
  embed.add_field(name="Arabic", value=arabic, inline=False)
  embed.add_field(name="English Translation", value=f"{english}\n\n**Grade: {hukm}**", inline=False)
    
  
  await ctx.send(embed=embed)        

    

@bot.event
async def on_ready():
    print("` بِسْمِ ٱللَّٰهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ`")
    print(f"We are ready--------\n{bot.user.name}\n---------\n{bot.user.id}")


    
   

keep_running()
bot.run(os.getenv('TOKEN'))


