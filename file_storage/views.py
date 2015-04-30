from django.shortcuts import render
from django.contrib import messages
from file_storage.models import ImageFile
from file_storage.forms import ImageFileForm
from PIL import Image
import os


def upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = ImageFile(image=request.FILES['image'])
            image_file.save()
            #ImageFile.create_thumbnail(image_file.file.path)

            # Redirect ... somewhere.
    else:
        form = ImageFileForm()

    try:
        thumbs = ImageFile.objects.order_by('date_created')[:5]
        if len(thumbs) == 0:
            raise ValueError
    except:
        messages.info(request, 'No existing image uploads were found.')
        thumbs = []

    context = {'form': form, 'thumbs': thumbs}
    return render(request, 'image-upload.html', context)
