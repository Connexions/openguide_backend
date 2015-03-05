from django.shortcuts import render
from django.contrib import messages
from file_storage.models import ImageFile
from file_storage.forms import ImageFileForm
from PIL import Image
import os

def create_thumbnail(image_file):
    """ This is not a view. This saves a thumbnail for an image. """
    filename, ext = os.path.splitext(image_file)
    thumb_image = Image.open(image_file)
    thumb_image.thumbnail((128, 128), Image.ANTIALIAS)
    thumb_image.save(filename+"_thumbnail.png", "PNG")

def upload(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = ImageFile(file=request.FILES['file'])
            image_file.save()
            create_thumbnail(image_file.file.path)

            # Redirect ... somewhere.
    else:
        form = ImageFileForm()

    try:
        images = ImageFile.objects.order_by('date_created')[:5]
        if len(images) == 0:
            raise ValueError
    except:
        messages.info(request, 'No existing image uploads were found.')
        images = []

    context = {'form': form, 'images': images}
    return render(request, 'image-upload.html', context)
