from datetime import date
now = date.today()
now

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
birthday = date(2001, 12, 13)
age = now - birthday
age.days