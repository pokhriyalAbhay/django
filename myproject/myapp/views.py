# myapp/views.py
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm

def handle_uploaded_file(file):
    try:
        # Read the Excel file
        df = pd.read_excel(file)
        
        # Rename the 'Cust State' column to 'State'
        df.rename(columns={'Cust State': 'State'}, inplace=True)
        
        # Group by 'State' and 'DPD', then count the occurrences
        summary = df.groupby(['State', 'DPD']).size().reset_index(name='Count')
        return summary
    except Exception as e:
        print(f"Error processing file: {e}")
        return None

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            summary = handle_uploaded_file(request.FILES['file'])
            if summary is not None:
                return render(request, 'myapp/summary.html', {'summary': summary.to_html()})
            else:
                return HttpResponse("There was an error processing the file.")
    else:
        form = UploadFileForm()
    return render(request, 'myapp/upload.html', {'form': form})
