from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonForm
from .models import PersonModel
# function based view

def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request, 'person.html', {'form': form})


def person_list(request):
    data = PersonModel.objects.all()
    return render(request, 'person_list.html', {'data': data})


def person_retrieve(request, pk):
    data = get_object_or_404(PersonModel, pk=pk)
    return render(request, 'person_detail.html', {'data': data})


def person_update(request, pk):
    person = get_object_or_404(PersonModel, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_retrieve', pk=pk) 
    else:
        form = PersonForm(instance=person) 
        print(form)
    
    return render(request, 'person_update.html', {'form': form})


def person_delete(request, pk):
    person = get_object_or_404(PersonModel, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'person_delete.html', {'object': person})


# class based view

class PersonCreateView(CreateView):
    model = PersonModel
    form_class = PersonForm
    template_name = 'person.html'
    success_url = reverse_lazy('person_list')

class PersonListView(ListView):
    model = PersonModel
    template_name = 'person_list.html'
    context_object_name = 'data'

class PersonRetrieveView(DetailView):
    model = PersonModel
    template_name = 'person_detail.html'
    context_object_name = 'data'

class PersonUpdateView(UpdateView):
    model = PersonModel
    form_class = PersonForm
    template_name = 'person_update.html'

    def get_success_url(self):
        return reverse_lazy('person_detail', kwargs={'pk': self.object.pk})

class PersonDeleteView(DeleteView):
    model = PersonModel
    template_name = 'person_delete.html'
    success_url = reverse_lazy('person_list')