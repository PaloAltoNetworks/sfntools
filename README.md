# SAFE NETWORKING TOOLS

## Install & run the app to get help on usage
### 1. Clone repo
```git clone https://www.github.com/PaloAltoNetworks/safe-networking-tools.git```
<br/>
### 2. Change into repo directory
```cd safe-networking-tools```
<br/>
### 3. Create python 3.6 virtualenv
#### NOTE: If you need to install python 3.6, see [these instructions](https://github.com/PaloAltoNetworks/safe-networking/wiki/Infrastructure-Setup---LOCAL#python-36)
```python3.6 -m venv env```
<br/>
### 4. Activate virtualenv
```source env/bin/activate```
<br/>
### 5. Download required libraries
```pip install -r requirements.txt```
<br/>
### 6. Run sfntools to see the usage instructions
```./sfntools```
<br/>

# Examples
#### Replay a log from home directory to a server with port 514
*./sfntools replay --host 192.168.17.222 --port 514 --log ~/mylog.csv*

#### Generate fake DNS data for last 60 days with 20 thousand events to localhost and default port 
*./sfntools dns --days_past 60 --tne 20000*

#### Get help for replay sub-command
*./sfntools replay --help*


#### If you need assistance, contact sp-solutions@paloaltonetworks.com