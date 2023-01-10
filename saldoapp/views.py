from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

from .models import *

import random

# Create your views here.

month_names = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь',
}

def home(response:HttpRequest):
    try:
        if response.method == 'POST':
            for apartment_id in range(1, 10):
                for year in (2017, 2018, 2019):
                    s = InitialSaldo()

                    s.apartment_id = apartment_id
                    s.value = random.uniform(0, 20000)
                    s.year = year

                    s.save()

            for apartment_id in range(1, 10):
                for year in (2017, 2018, 2019):
                    for month in range(1, 12 + 1):
                        p = Payment()
                        p.apartment_id = apartment_id
                        p.value = random.uniform(0, 20000)
                        p.year = year
                        p.month = month

                        p.save()

                        c = Charge()
                        c.apartment_id = apartment_id
                        c.value = random.uniform(0, 20000)
                        c.year = year
                        c.month = month

                        c.save()
    except: pass

    return render(response, 'home.html', {})

def init_saldo(response:HttpRequest):
    error_message = ''

    if response.method == 'POST':
        try:
            apartment_id = int(response.POST.get('apartment_id'))
            value = float(response.POST.get('value'))
            year = float(response.POST.get('year'))

            o = InitialSaldo()

            o.apartment_id = apartment_id 
            o.value = value
            o.year = year

            o.save()
        except:
            if len(error_message) == 0:
                error_message = 'Ошибка! Проверьте корректность данных и попробуйте еще раз'

    table = InitialSaldo.objects.order_by('apartment_id')
    return render(response, 'init_saldo.html',
                  {'table': table,
                   'error_orccured': len(error_message) != 0,
                   'error_message': error_message})

def payments(response:HttpRequest):
    error_message = ''
    filter_used = False

    if response.method == 'POST':
        try:
            apartment_id = int(response.POST.get('apartment_id'))
            value = float(response.POST.get('value'))
            month = int(response.POST.get('month'))
            year = int(response.POST.get('year'))
            print(1)

            # Проверка на корректность данных
            if value <= 0:
                error_message = 'Указано значение платежа меньше или равное 0'
                raise Exception()

            if month < 1 or month > 12:
                error_message = 'Указано некорректное значение месяца'
                raise Exception()

            o = Payment()

            print(1)

            o.apartment_id = apartment_id
            o.value = value 
            o.month = month
            o.year = year

            print(1)

            o.save()

            print(1)
        except:
            if len(error_message) == 0:
                error_message = 'Ошибка! Проверьте корректность данных и попробуйте еще раз'

    elif response.method == 'GET':
        # Если пользователь воспользовался фильтром
        if len(list(response.GET)) > 0:
            try:
                from_year = response.GET.get('from_year')
                to_year = response.GET.get('to_year')
                from_month = response.GET.get('from_month')
                to_month = response.GET.get('to_month')

                table = Payment.objects.filter(year__gte=from_year, year__lte=to_year)
                table = table.filter(month__gte=from_month, month__lte=to_month)

                try:
                    table = table.filter(apartment_id=response.GET.get('apartment_id'))
                except:
                    pass



                table = table.order_by('apartment_id', 'year', 'month')[::-1]
                filter_used = True
            except:
                if len(error_message) == 0:
                    error_message = 'Ошибка! Неверно заданы параметры фильтра'


    if not filter_used:
        table = Payment.objects.order_by('apartment_id', 'year', 'month')[::-1]

    return render(response, 'payments.html',
                  {'table': table,
                   'error_orccured': len(error_message) != 0,
                   'error_message': error_message,
                   'month_names': month_names})

def charges(response):
    error_message = ''
    filter_used = False

    if response.method == 'POST':
        try:
            apartment_id = int(response.POST.get('apartment_id'))
            value = float(response.POST.get('value'))
            month = int(response.POST.get('month'))
            year = int(response.POST.get('year'))

            # Проверка на корректность данных
            if value <= 0:
                error_message = 'Указано значение платежа меньше или равное 0'
                raise Exception()

            if month < 1 or month > 12:
                error_message = 'Указано некорректное значение месяца'
                raise Exception()

            o = Charge()

            o.apartment_id = apartment_id
            o.value = value
            o.month = month
            o.year = year

            o.save()
        except:
            if len(error_message) == 0:
                error_message = 'Ошибка! Проверьте корректность данных и попробуйте еще раз'

    elif response.method == 'GET':
        # Если пользователь воспользовался фильтром
        if len(list(response.GET)) > 0:
            try:
                from_year = response.GET.get('from_year')
                to_year = response.GET.get('to_year')
                from_month = response.GET.get('from_month')
                to_month = response.GET.get('to_month')

                table = Payment.objects.filter(year__gte=from_year, year__lte=to_year)
                table = table.filter(month__gte=from_month, month__lte=to_month)

                try:
                    table = table.filter(apartment_id=response.GET.get('apartment_id'))
                except:
                    pass

                table = table.order_by('apartment_id', 'year', 'month')[::-1]
                filter_used = True
            except:
                if len(error_message) == 0:
                    error_message = 'Ошибка! Неверно заданы параметры фильтра'

    if not filter_used:
        table = Charge.objects.order_by('apartment_id', 'year', 'month')[::-1]

    return render(response, 'charges.html',
                  {'table': table,
                   'error_orccured': len(error_message) != 0,
                   'error_message': error_message,
                   'month_names': month_names})

def apartment(response):
    error_message = ''
    filter_used = False

    if response.method == 'GET':
        # Если пользователь воспользовался фильтром
        if len(list(response.GET)) > 0:
            try:
                year = response.GET.get('year')
                apartment_id = response.GET.get('apartment_id')

                table = {}

                init_saldo = InitialSaldo.objects.get(apartment_id=apartment_id, year=year).value
                table['init_saldo'] = init_saldo

                list_payments = [0,] * 12
                payments_sum = 0

                list_charges = [0,] * 12
                charges_sum = 0

                payments = Payment.objects.filter(apartment_id=apartment_id, year=year)

                for p in payments:
                    list_payments[p.month-1] = p.value
                    payments_sum += p.value

                charges = Charge.objects.filter(apartment_id=apartment_id, year=year)

                for c in charges:
                    list_charges[c.month-1] = c.value
                    charges_sum += c.value

                table['list_payments'] = list_payments
                table['list_charges'] = list_charges

                table['payments_sum'] = payments_sum
                table['charges_sum'] = charges_sum

                print(table)

                table['result'] = payments_sum - charges_sum + init_saldo

                filter_used = True
            except:
                if len(error_message) == 0:
                    error_message = 'Ошибка! Неверно заданы параметры фильтра'

    if not filter_used:
        table = {}


    return render(response, 'apartment.html',
                  {'table': table,
                   'filter_used': filter_used,
                   'error_orccured': len(error_message) != 0,
                   'error_message': error_message,})

def year_result(response):
    error_message = ''
    filter_used = False
    apartments = {}
    apartment_ids = []

    if response.method == 'GET':
        # Если пользователь воспользовался фильтром
        if len(list(response.GET)) > 0:
            try:
                year = response.GET.get('year')
                apartment_ids = str(response.GET.get('apartment_ids')).split(' ')

                for i, a in enumerate(apartment_ids):
                    apartment_ids[i] = int(a)

                for apartment_id in apartment_ids:
                    table = {}

                    init_saldo = InitialSaldo.objects.get(apartment_id=apartment_id, year=year).value
                    table['init_saldo'] = init_saldo

                    list_payments = [0,] * 12
                    payments_sum = 0

                    list_charges = [0,] * 12
                    charges_sum = 0

                    list_saldos = [0, ] * 12

                    payments = Payment.objects.filter(apartment_id=apartment_id, year=year)

                    for p in payments:
                        list_payments[p.month-1] = p.value
                        payments_sum += p.value

                    charges = Charge.objects.filter(apartment_id=apartment_id, year=year)

                    for c in charges:
                        list_charges[c.month-1] = c.value
                        charges_sum += c.value

                    last_saldo = init_saldo
                    for i in range(1, 12+1):
                        last_saldo += list_payments[i-1]
                        last_saldo -= list_charges[i-1]
                        list_saldos[i-1] = last_saldo

                    table['list_payments'] = list_payments
                    table['list_charges'] = list_charges

                    table['payments_sum'] = payments_sum
                    table['charges_sum'] = charges_sum

                    table['list_saldos'] = list_saldos

                    table['result'] = payments_sum - charges_sum + init_saldo

                    apartments[apartment_id] = table

                    filter_used = True
            except:
                if len(error_message) == 0:
                    error_message = 'Ошибка! Неверно заданы параметры фильтра'

    if not filter_used:
        apartments = {}

    print(apartments)

    return render(response, 'year_result.html',
                  {'apartments': apartments,
                   'filter_used': filter_used,
                   'apartment_ids': apartment_ids,
                   'error_orccured': len(error_message) != 0,
                   'error_message': error_message,})