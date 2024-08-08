from django.shortcuts import render

from django.contrib.auth.decorators import permission_required

from .forms import FormThemen

from .models import Lerneinheit

# Create your views here.

@permission_required('plan.view_lerneinheit')
def edtLerneinheit(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = FormThemen(request.POST)
        # check whether it's valid:
        if form.is_valid():
            thema = form.cleaned_data["thema"]
            # return HttpResponseRedirect("/thanks/")
            einheiten = Lerneinheit.objects.filter(field=thema).order_by("position")
    else:
        form = FormThemen()
        einheiten = None
    content = {
        'form': form,
        'einheiten': einheiten,
    }
    return render(request, 'edtle.html', content)
