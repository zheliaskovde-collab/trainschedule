from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Route, Station


def home_view(request):
    return render(request, 'core/index.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            default_group = Group.objects.get_or_create(name='Пасажири')
            user.groups.add(default_group)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        
    return render(request, 'core/register.html', {'form': form})




def schedule_list_view(request):
    is_vip = request.user.is_authenticated and request.user.groups.filter(name='VIP').exists()

    routes = Route.objects.all()
    stations_all = Station.objects.all()
    
    from_station_id = request.GET.get('from_station')
    to_station_id = request.GET.get('to_station')

    if from_station_id and to_station_id:
        valid_route_ids = []
        
        for route in routes:

            from_point = route.points.filter(station_id=from_station_id).first()
            to_point = route.points.filter(station_id=to_station_id).first()

            if from_point and to_point and from_point.station_order < to_point.station_order:
                valid_route_ids.append(route.id)

        routes = routes.filter(id__in=valid_route_ids)
        
    context = {
        'routes': routes,
        'stations_all': stations_all, 
        'is_vip': is_vip,
    }
    return render(request, 'core/schedule_list.html', context)