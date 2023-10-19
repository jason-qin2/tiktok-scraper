FROM python:3.9

ADD scraper.py .

RUN pip install tiktokapipy
RUN python -m playwright install
RUN playwright install-deps 

CMD [ "python", "./scraper.py"]