from django.shortcuts import render, redirect
from django.contrib import auth


def logouts(request):
    auth.logout(request)
    return redirect('/')
