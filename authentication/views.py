from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect,HttpResponse
import cx_Oracle


def oracle_authentication(username, password):
    try:
        dsn = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 1017:
            return None
        else:
            raise
    return authenticate(username=username, password=password)


def login_page(request):
    message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = oracle_authentication(username, password)
            if user is not None:
                login(request, user)
                response = redirect('home')
                response.set_cookie('username', username)
                response.set_cookie('password', password)
                return response
            else:
                message = "Nom d'utilisateur ou mot de passe incorrect."
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form , 'message':message} )



def oracle_connect(username, password):
    try:
        dsn = cx_Oracle.makedsn('localhost', '1521', service_name='orcl')
        connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        if error.code == 1017:
            return None
        else:
            raise
    return connection

def select(request):
    connection = oracle_connect(request.COOKIES.get('username'), request.COOKIES.get('password'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM produits")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return render(request, 'authentication/select.html', {'data': data})


def logout_user(request):
    logout(request)
    return redirect('login')

def insert(request):
    connection = oracle_connect(request.COOKIES.get('username'), request.COOKIES.get('password'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO produits (id, nom, prix, quantite) VALUES (4, 'Ordinateur', 1000, 5)")
    connection.commit()
    cursor.close()
    connection.close()
    message = "Données insérées avec succès"
    return render(request, 'authentication/insert.html', {'message': message})

def update(request):
    connection = oracle_connect(request.COOKIES.get('username'), request.COOKIES.get('password'))
    cursor = connection.cursor()
    cursor.execute("UPDATE produits SET nom = 'Mangue', prix = 12.99, quantite = 20 WHERE id = 1")
    connection.commit()
    cursor.close()
    connection.close()
    message = "Données mises à jour avec succès"
    return render(request, 'authentication/update.html', {'message':message})

@login_required
def home(request):
    return render(request,'authentication/home.html',{'user':request.user})