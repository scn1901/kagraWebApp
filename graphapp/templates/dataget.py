#Fukuoka Daigaku ip : 133.100.214.16
#kagra ip : 192.168.200.6
def getData(): 
	from gwpy.timeseries import TimeSeries
	ch="K1:CAL-CS_PROC_DARM_STRAIN_DBL_DQ"
	start=1361343353
	end=start+10
	data = TimeSeries.get(ch, start, end, host="192.168.200.6", port=31200) 
	return data