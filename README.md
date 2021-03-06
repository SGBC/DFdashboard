# DairyFarmersDashboard
A Dashboard providing farmers with a Dashboard accessing data from Gigacow. A list of features to be added are available in Missing.txt.

For production servers remove the secret in DFdashboard/interfaces/DjangoDashboard/mysite/settings.py


## Back end
* The functions folder is a package containing all the modules needed for computing the key values.
* The data processing library pandas is used which means that all data (inputs/outputs) is handled as pandas DataFrames.
* The functions need specific inputs which is described for every function in each module as well as what the output will be.
* Make sure to locate the correct folder when running the "Main" script (mostly directed at Windows users). Otherwise the CSV files
might not be found (Out of Index error). Main should be run in the same folder as the 'extractions' folder.
* A warning "A value is trying to be set on a copy of a slice from a DataFrame" may appear but does not prevent Main.py from running.


## Front end
* Our dashboard is in interfaces/DjangoDashboard
* To run the fron end, the Python libraries Django, django-echarts, must be installed.
* cd into the folder, using 'python manage.py runserver' to view the dashboard. :)
* To show the dashboard, please visit http://127.0.0.1:8000/index/
* The dashboard has been tested both on Microsoft Edge or Google Chrome browsers with screen size 1920*1080.
* It is a demo dashboard. We tried to implement a more functional dashboard that you can check more details by mouse over the diagrams.
* To install django-echarts: npm install echarts --save
