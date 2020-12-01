import subprocess
import time
import datetime
#import chart_studio.plotly
#import chart_studio.plotly.plotly as py
#import chart_studio.plotly.graph_objs as go
import pandas as pd

###########################
#
# config
#
###########################



#plotlyusername = "username"
#plotlyapi = "apt-key"

# Get server id from speedtest-cli --list
# Maybe good idea to pipe result into head -n # to get servers near you.
# speedtest-cli --list | head -n 10
server = "speedtest --server 3628 --csv"
# First 3 first fields of result csv to indicate what server is given issues, if using multiple servers.

server1error = "3628,SE,Sonderborg"

pinglowerbound = 0
pingupperbound = 2000
# units are in bits/s so 150000000 is 150 Mbit/s
bandwidthlowerbound = 0
bandwidthupperbound = 120000000

plotfilename = "Plot Name"
plottitle = "Plot Titel"

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
    process = subprocess.Popen(server.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print (output)
if ("Cannot" in str(output)):
    writeerror(server1error,output)
    process = subprocess.Popen(server.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
if ("Cannot" in str(output)):
    writeerror(server1error, output)
    process = subprocess.Popen(server.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
if ("Cannot" in str(output)):
    writeerror(server1error, output)
    output = server1error + datetime.datetime.fromtimestamp(time.time()).strftime(
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
'''
plotly.tools.set_credentials_file(username=plotlyusername, api_key=plotlyapi)
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
    title=plottitle,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1d',
                     step='day',
                     stepmode='backward'),
                dict(count=7,
                     label='7d',
                     step='day',
                     stepmode='backward'),
                dict(count=14,
                     label='14d',
                     step='day',
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
        range=[bandwidthlowerbound, bandwidthupperbound]
    ),
    yaxis2=dict(
        title='ms latency',
        range=[pinglowerbound, pingupperbound],
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

#data = [download, upload, ping]
#fig = dict(data=data, layout=layout)

#url = py.plot(fig, filename=plotfilename, auto_open=False)
#print(url)
# plotembed = ("<iframe width=\"1900\" height=\"840\" frameborder=\"0\" scrolling=\"no\" src=\"" + url +".embed\"></iframe>")
# fd = open('/var/www/html/speedtestplot.php')
# fd.write(plotembed)
# fd.close()
'''

