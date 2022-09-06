from django.shortcuts import render, redirect
from django.views import View
from .models import Food, CalorieConsume


class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        foods = Food.objects.all()
        consumed_food = CalorieConsume.objects.filter(user=request.user)
        context = {"foods": foods, "consumed_food": consumed_food}
        return render(request, self.template_name, context)

    def post(self, request):
        food_consumed = request.POST["food_consumed"]
        consume = Food.objects.get(item=food_consumed)
        user = request.user
        consume = CalorieConsume(user=user, food_consumed=consume)
        consume.save()
        return redirect("/")


class DeleteView(View):
    template_name = "delete.html"

    def get(self, request, id):
        consumed_food = CalorieConsume.objects.get(id=id)
        context = {"consumed_food": consumed_food}
        return render(request, self.template_name, context)

    def post(self,request, id):
        consumed_food = CalorieConsume.objects.get(id=id)
        consumed_food.delete()
        return redirect("/")


class AddView(View):
    template_name = "forms.html"

    def get(self, request):
        form = Food()
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request):
        item = request.POST["item"]
        carbohydrates = request.POST["carbohydrates"]
        fats = request.POST["fats"]
        calories = request.POST["calories"]
        proteins = request.POST["proteins"]
        food = Food(
            item=item,
            carbohydrates=carbohydrates,
            proteins=proteins,
            fats=fats,
            calories=calories,
        )
        food.save()
        return redirect("/")
