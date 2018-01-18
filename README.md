# Speedtester
Had some problems with my isp not giving me the speed i paid for. so made a script to log the speed every 15 minutes.

An exsameple of the plot generated can be seen at https://doommius.com/speedtest.php

Works with python3.6

packages required are.

plotly, pandas and speedtest-cli

They can be installed from pip via
```
sudo -H pip3 install plotly
sudo -H pip3 install pandas
sudo -H pip3 install speedtest-cli
```

An example of a crontab to run the code every 15 minutes has been included.

