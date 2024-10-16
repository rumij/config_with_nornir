import pandas as pd
dev = pd.read_excel('inventory.xlsx')
device = dev.to_dict(orient='records')

