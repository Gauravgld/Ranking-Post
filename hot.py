from datetime import datetime, timedelta
from math import log

def hot(likes,views,pdate)
	td = datetime.today() - pdate
	day = td.days * 86400 + td.seconds + (float(td.microseconds) / 1000000)
	s = (views-likes)/2
	order = log(max(abs(s), 1), 10)
	sign = 1 if s > 0 else -1 if s < 0 else 0
	seconds = day - 1134028003
	return(int(sign * order + seconds / 45000))