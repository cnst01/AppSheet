import setup.sheettools as sheettools
import setup.quickstart as quickstart

quickstart.main()
fullsheet = sheettools.get_values("1L3U0sS7mw3recPfoagh2ws-DrHLhse_S-v5ckjKDm2U","3ª Livre!A6:G34")
sheetvalues = fullsheet.get('values')
for i in range(len(sheetvalues)):
    print(sheetvalues[i][:])
    
sheettools.write_values("1HgRkyNAlw6NZAh8WCK-ZpF6F81VPTqpodDDa-Mwlh4M","A6:G34","USER_ENTERED",sheetvalues)




