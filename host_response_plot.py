import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('listings.csv')
df_resp_time = df['host_response_time']
df_resp_time.value_counts().plot.bar()
plt.ylabel('Count')
plt.xlabel('Host Response Time')
plt.xticks(rotation='horizontal')
plt.title('Histogram of Hosts\' Response Time')
plt.savefig('resp_time.png')
plt.show()

df_resp_rate = df['host_response_rate']
df_resp_rate = df_resp_rate.str.replace("%", "").astype("float")
df_resp_rate.hist(bins=20)
plt.ylabel('Count')
plt.xlabel('Host Response Rate (in %)')
plt.title('Histogram of Hosts\' Response Rate')
plt.savefig('resp_rate.png')
plt.show()
