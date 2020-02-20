# python-download-retry

The Python Download Retry script implements an easy way to handle retry operation to download a file through web.

This is common use for synchronize and be sure that an file will be downladed.

### Use Example
The script expects two parameters first the url to file and second the absolute path to save the file
```
python download-retry.py http://www.rdtecnologia.com.br/wp-content/themes/tema/js/jquery-1.4.2.min.js /home/jquery.js
```
You be able to configure the retring interval in this parameters **wait_random_min** and **wait_random_max**
```
@retry(wait_random_min=1000, wait_random_max=2000)
```
If you wonder to know how this @entry decorator works, see it here https://pypi.python.org/pypi/retrying
