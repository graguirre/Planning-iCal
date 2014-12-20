import datetime
from isoweek import Week

# date to string
def dtos(h):
	return str(h.year)+str(h.month).zfill(2)+str(h.day).zfill(2)
# hour to string
def htos(f):
        h,m = divmod(f,1)
        if len(str(int(60*m))) == 1:
                min = '00'
        else:
                min = '30'
        return str(int(h)).zfill(2)+min+'00'


fd = open('horario.txt')

ll=[]
l=[]
ind=0
for i in fd:
	ll.append(i.strip())
	if (ind+1)%48 == 0:
		l.append(ll)
		ll = []
	ind+=1

#print l

f=[]

fd = open('semana.txt')
for i in fd:
	f = Week(2014,int(i.strip())).monday()


print "BEGIN:VCALENDAR"
print "VERSION:1.0"

hoy = f
dia = 0
ent = -1
for i in l:
	tmp = hoy + datetime.timedelta(days=dia)
	for j in range(len(i)-1):
		if i[j] != i[j+1] and ent == -1:
			ent = j+1
		elif i[j] != i[j+1] :
			print "BEGIN:VEVENT"
			print "CATEGORIES:APPOINTMENT"
			print "STATUS:ACCEPTED"
#			hora UTC +01 (+02 en verano)
			print "DTSTART:"+dtos(tmp)+"T"+htos(6.0+float(ent)/2)+"+01"
			print "DTEND:"+dtos(tmp)+"T"+htos(6.5+float(j)/2)+"+01"
#			print ent,' -- ',j		
			print "SUMMARY:Decathlon"
			print "DESCRIPTION:Go to work"
			print "CLASS:PRIVATE"
			print "END:VEVENT"
			ent = -1
	dia += 1

print "END:VCALENDAR"


