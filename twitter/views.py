from .models import Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect,render,reverse
from django.views import View



class IndexView(View):
    def get(self, request):
        messages = Message.objects.all()
        return render(request, "index.html", {"messages":messages[::-1]})

    def post(self, request):
        text = request.POST["text"]
        message = Message(
            text = text,
            author = request.user,
        )
        message.save()
        return redirect(reverse("index"))

class AuthView(View):
    def get(self,request):
        return render(request, "auth.html")

    def post(self, request):
        #print("data:",request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        action = request.POST["action"]

        if action == "signin":
            return self.signin(request, username,password)
        elif action == "signup":
            return self.signup(request, username, password)


    def signin(self, request, username,password):
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
        return redirect(reverse("index"))


    def signup(self, request, username,password):
        user = User.objects.create_user(
            username=username,
            password=password

        )
        login(request,user)
        return redirect(reverse("index"))




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("index"))
