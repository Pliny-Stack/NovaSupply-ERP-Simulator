

import pandas as pd

shipments = pd.read_csv("output/bronze/FactShipment.csv")

result = shipments.groupby("Status")["ActualDeliveryDate"].apply(lambda x: x.isna().sum())

print(result)