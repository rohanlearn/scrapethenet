from django.http import FileResponse

def download_file(request):
    file_path = '/path/to/file.txt'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="file.txt"'
    return response

