import os
import pdb
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from functools import reduce
import stripe
from showcase.models import Item

load_dotenv('.env')
stripe.api_key = os.environ.get('STRIPE_PRIVATE_KEY')

DOMAIN = os.environ.get('DOMAIN')


def item(request, pk):
    pk = int(pk)-1
    item = Item.objects.all()[pk].name
    description = Item.objects.all()[pk].description
    price = Item.objects.all()[pk].price
    context = {
        'item': item,
        'description': description,
        'price': price,
        'id': str(pk)
    }
    return render(request, 'checkout.html', context)

@csrf_exempt
def create_checkout_session(request, pk):
    item = Item.objects.all()[pk].name
    price = Item.objects.all()[pk].price * 100
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'USD',
                'product_data': {
                    'name': item,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=DOMAIN + '/success.html',
        cancel_url=DOMAIN + '/cancel.html',
    )
    return JsonResponse({'id': session.id})


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')

def view_info(request):
    objs=Item.objects.all()
    return render(request,'index.html',{'objs':objs})
