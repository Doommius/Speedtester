import subprocess
import time
import datetime
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

###########################
#
# config
#
###########################

server1 = "speedtest --server 3628 --csv"
server1error = "3628,SE,Sonderborg"
server2 = "speedtest --server 4435 --csv"
server3 = "speedtest --server 8763 --csv"
pinglowerbound = 0
pingupperbound = 1000
bandwidthupperbound = 150000000
bandwidthlowerbound = 0

###########################
#
# speedtest
#
###########################


def writeerror(errormsg, outputmsg):
    fd = open('error.csv', 'a')
    error = errormsg + datetime.datetime.fromtimestamp(time.time()).strftime(
        '%Y-%m-%dT%H:%M:%S') + ", Error, " + outputmsg
    fd.write(str(error))
    fd.close()
output = ""
if (True):
    process = subprocess.Popen(server1.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print (output)
if ("Cannot" in str(output)):
    writeerror(server1error,output)
    process = subprocess.Popen(server1.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
if ("Cannot" in str(output)):
    writeerror(server1error, output)
    process = subprocess.Popen(server1.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
if ("Cannot" in str(output)):
    writeerror(server1error, output)
    output = "3628,SE,Sonderborg," + datetime.datetime.fromtimestamp(time.time()).strftime(
        '%Y-%m-%dT%H:%M:%S') + "Z,0,0,0,0"
output =(str(output)[2:])[:-3]
print(output)
fd = open('/var/www/data/results.csv', 'a')
fd.write(output+"\n")
fd.close()


###########################
#
#Start Plotting
# Header infomation is "Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload"
###########################
plotly.tools.set_credentials_file(username='username', api_key='apt-code')
df = pd.read_csv('/var/www/data/results.csv')
upload = go.Scatter(
    x=df["Timestamp"],
    y=df["Upload"],
    name="Upload Speed",
    line=dict(color='#1f77b4'),
    opacity=0.8
)

download = go.Scatter(
    x=df["Timestamp"],
    y=df["Download"],
    name="Download Speed",
    line=dict(color='#00cc00'),
    opacity=0.8
)
ping = go.Scatter(
    x=df["Timestamp"],
    y=df["Ping"],
    name="Latency(ms)",
    yaxis='y2',
    line=dict(color='#d62728'),
    opacity=0.8)
layout = dict(
    title='Network Speed for SE Sonderborg server',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1w',
                     step='week',
                     stepmode='backward'),
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    ),
    yaxis=dict(
        title='bit/s',
        range=[0, 150000000]
    ),
    yaxis2=dict(
        title='ms latency',
        titlefont=dict(
            color='d62728'
        ),
        tickfont=dict(
            color='d62728'
        ),
        overlaying='y',
        side='right'
    )
)

data = [download, upload, ping]
fig = dict(data=data, layout=layout)

url = py.plot(fig, filename="networkspeed", auto_open=False)
print(url)
plotembed = ("<iframe width=\"1900\" height=\"840\" frameborder=\"0\" scrolling=\"no\" src=\"" + url +".embed\"></iframe>")
fd = open('/var/www/html/speedtestplot.php')
fd.write(plotembed)
fd.close()
