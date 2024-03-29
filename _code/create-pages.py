import datetime, calendar

def generate_dates(start_date, end_date):
    alldates = []
    td = datetime.timedelta(hours=24)
    current_date = start_date
    while current_date <= end_date:
        alldates.append(current_date)
        current_date += td
    return alldates

# January, 2013 is a Tuesday
start_date = datetime.date(2013, 1, 8)
end_date = datetime.date(2013, 4, 26)
tuesdays = generate_dates(start_date, end_date)

def getMonthName(date):
  d = dict((k,v) for k,v in enumerate(calendar.month_abbr))
  return d[date.month]

def getDayNumber(date):
  return date.day

def make_day (directory, day, date):
  pg = open ('%s/%s.md' % (directory, date), 'w')
  #pg.write('---\n')
  #pg.write('title: %s, %s\n' % (day, date))
  #pg.write('day: %s\n' % day)
  #pg.write('date: %s\n' % date)
  #pg.write('layout: minimal\n')
  #pg.write('---\n\n')
  #pg.write('# %s, %s %s' % (day, getMonthName(date), getDayNumber(date)))
  pg.write ('<!-- %s %s %s -->\n\n' % (date.strftime("%A"), getMonthName(date), getDayNumber(date)))
  pg.close()
  
def pad (n, places):
  i = places - len(str(n))
  padding = ""
  while i > 0:
    padding = '0%s' % padding
    i -= 1
  result = '%s%s' % (padding, n)
  return result
  
def make_week (directory, date, week_number, delta, count):
  pg = open ('%s/week-%s.md' % (directory, pad(week_number, 2)), 'w')
  #pg.write('---\n')
  #pg.write('title: Week %s \n' % week_number)
  #pg.write('week: %s\n' % week_number)
  #pg.write('date: %s\n' % date)
  #pg.write('layout: minimal\n')
  #pg.write('---\n\n')
  pg.write('# Week %s\n\n\n\n' % (week_number))
  

  while count > 0:
    day_of_week = date.strftime("%A")
    pg.write('## %s, %s %s\n\n' % (day_of_week, getMonthName(date), getDayNumber(date)))
    pg.write('{%% include days/%s.md %%}\n\n' % date)
    date += datetime.timedelta(hours = (24*delta))
    count -= 1
  
  pg.close()

i = 0
week_number = 1
while (i < len(tuesdays)):
  print tuesdays[i]
  make_day('days', 'Tuesday', tuesdays[i])
  make_week('weeks', tuesdays[i], week_number, 2, 2)
  week_number += 1
  i += 2
  print tuesdays[i]
  make_day('days', 'Thursday', tuesdays[i])
  i += 5
