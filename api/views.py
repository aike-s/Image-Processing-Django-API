import json
from django.views import View
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import History, Job
from .tasks import Tasks
from .forms import JobForm


class JobView(View):
    """  """

    def get(self, request, id=0):
        """ Check all history of a job """

        job_history = list(History.objects.filter(job_id=id).values())

        if id <= 0 or job_history.count == 0:
            data = {"message":"History not found"}

        else:
            data = {
                "jobId": id,
                "steps": job_history
            }

        return JsonResponse(data)


    def post(self, request):
        """ Create a new job to create an image """

        form = JobForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            # Getting the current instance object to display in the template  
            img_object = form.instance
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  

        else:  
            form = JobForm()

        return render(request, 'image_form.html', {'form': form})  


    def put(self, request, id, step):
        """ Changes the status of a job to the user's desired step """
        # PUT ACTIONS
        # Se crea cada dato de History
        # Se utiliza una funcion determinada para alterar la imagen
        job = list(Job.objects.filter(id=id).values())

        if id <= 0 or job.count == 0:
            data = {"message":"Id not found"}


class HistoryView(View):

    def get(self, request):
        """ Check all images history """
        history = list(History.objects.values())

    def post(self, request):
        """  """
        form = JobForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            # Getting the current instance object to display in the template  
            img_object = form.instance
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  

        else:  
            form = JobForm()

        return render(request, 'image_form.html', {'form': form})  


