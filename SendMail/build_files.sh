echo " BUILD START"
source myenv/bin/activate
python3.9 -m pip install or requirements.txt
python3.9 manage.py collectstatic - - noinput --clear
echo " BUILD END"