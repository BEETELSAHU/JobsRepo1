import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')

import django
django.setup()

from faker import Faker
from random import *
from testapp.models import *

f = Faker()

def pn_gen():
    d1 = randint(6,9)
    num = ''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def f1(n):
    for i in range(n):
        fdate = f.date()
        fcompany = f.company()
        ftitle = f.random_element(elements=('Project Manager','Team Lead','Software Engineer','HR','Associate Engineer','System Engineer','Data Analyst','Testers'))
        felg = f.random_element(elements=('Any Graduate','B.E/B.Tech','B.Sc','MCA','BCA','MBA'))
        faddr = f.address()
        femail = f.email()
        fpno = pn_gen()
        HydJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=felg, address=faddr, email=femail, phonenumber=fpno)
    print(f'In Hyderabad Database table {n} rows inserted sccessfully.')

def f2(n):
    for i in range(n):
        fdate = f.date()
        fcompany = f.company()
        ftitle = f.random_element(elements=('Project Manager','Team Lead','Software Engineer','HR','Associate Engineer','System Engineer','Data Analyst','Testers'))
        felg = f.random_element(elements=('Any Graduate','B.E/B.Tech','B.Sc','MCA','BCA','MBA'))
        faddr = f.address()
        femail = f.email()
        fpno = pn_gen()
        BngJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=felg, address=faddr, email=femail, phonenumber=fpno)
    print(f'In Bangalore Database table {n} rows inserted sccessfully.')
    
def f3(n):
    for i in range(n):
        fdate = f.date()
        fcompany = f.company()
        ftitle = f.random_element(elements=('Project Manager','Team Lead','Software Engineer','HR','Associate Engineer','System Engineer','Data Analyst','Testers'))
        felg = f.random_element(elements=('Any Graduate','B.E/B.Tech','B.Sc','MCA','BCA','MBA'))
        faddr = f.address()
        femail = f.email()
        fpno = pn_gen()
        PuneJobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=felg, address=faddr, email=femail, phonenumber=fpno)
    print(f'In Pune Database table {n} rows inserted sccessfully.')

while True:
    print('********************* Cities Menu ************************')
    print('\t1 -> Hyderabad\n\t2 -> Bangalore\n\t3 -> Pune\n\t4 -> Exit(enough data inserted!!).\n\n')
    ch = int(input('Choose one fron above:'))
    if ch==1:
        n=int(input('Enter jobs available at Hyderabad -> '))
        f1(n)
    elif ch==2:
        n=int(input('Enter jobs available at Bangalore -> '))
        f2(n)
    elif ch==3:
        n=int(input('Enter jobs available at Pune -> '))
        f3(n)
    else:
        print('Thanks.....')
        os._exit(1)