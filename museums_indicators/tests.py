from datetime import datetime
from .api_connections import RequestMuseumRawData
from .models import LastUpdateMuseumDate
from .models import MuseumData
from .models import MuseumArea
from .models import MuseumTags
from .models import LastUpdateMuseumDate
from .views import populate_museum_data
from quero_cultura.views import ParserYAML
import requests_mock
import json


class TestLastUpdateMuseumDate(object):
    def test_last_update_museum_date(self):
        LastUpdateMuseumDate.drop_collection()
        create_date = datetime.now().__str__()
        LastUpdateMuseumDate(create_date).save()
        query = LastUpdateMuseumDate.objects.first()
        assert query.create_date == create_date


class TestMuseumArea(object):
    def test_museum_area(self):
        MuseumArea.drop_collection()
        instance = "SP"
        area = "Cinema"
        MuseumArea(instance, area).save()
        query = MuseumArea.objects.first()
        assert query.instance == instance
        assert query.area == area


class TestMuseumTags(object):
    def test_museum_area(self):
        MuseumTags.drop_collection()
        instance = "SP"
        tag = "OlavoBilac"
        MuseumTags(instance, tag).save()
        query = MuseumTags.objects.first()
        assert query.instance == instance
        assert query.tag == tag


class TestMuseumData(object):
    def test_museum_data(self):
        MuseumData.drop_collection()
        instance = "SP"
        museum_type = "Cia"
        accessibility = "Sim"
        date = datetime(2017, 11, 14, 3, 5, 55, 88000)

        MuseumData(instance, museum_type, accessibility, date).save()
        query = MuseumData.objects.first()
        assert query.instance == instance
        assert query.museum_type == museum_type
        assert query.accessibility == accessibility
        assert query.date == date


class TestRequestMuseumRawData(object):
    @requests_mock.Mocker(kw='mock')
    def test_request_museum_raw_data(self, **kwargs):
        url = "http://mapas.cultura.gov.br/api/"

        result = [{"createTimestamp": {"date": "2012-01-01 00:00:00.000000"},
                   "acessibilidade": "Sim",
                   "type": {"id":"60", "name":"Museum Publico"},
                   "terms": {"area": ["Cinema", "Teatro"], "tag":["Olavo Bilac"]}}]

        kwargs['mock'].get(url+"space/find/", text=json.dumps(result))

        current_time = datetime.now().__str__()
        raw_data = RequestMuseumRawData(current_time, url)
        assert raw_data.response.status_code == 200
        assert raw_data.data == result
        assert raw_data.data_length == 1


class TestPopulateMuseumData(object):
    @requests_mock.Mocker(kw='mock')
    def test_populate_museum_data(self, **kwargs):
        parser_yaml = ParserYAML()
        urls = parser_yaml.get_multi_instances_urls

        result = [{"createTimestamp": {"date": "2012-01-01 00:00:00.000000"},
                   "acessibilidade": "Sim",
                   "type": {"id":"60", "name":"Museum Publico"},
                   "terms": {"area": ["Cinema", "Teatro"], "tag":["Olavo Bilac"]}}]

        for url in urls:
            kwargs['mock'].get(url + "space/find/", text=json.dumps(result))

        LastUpdateMuseumDate.drop_collection()
        MuseumData.drop_collection()
        MuseumArea.drop_collection()
        MuseumTags.drop_collection()

        populate_museum_data()

        assert LastUpdateMuseumDate.objects.count() != 0
        assert MuseumData.objects.count() != 0
