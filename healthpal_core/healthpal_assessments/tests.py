from datetime import timedelta, date

from django.contrib.auth.models import User
from django.utils import timezone
from django.test import RequestFactory
from healthpal_patients.models import Patient, GenderChoices
from healthpal_shared.tests import BaseSerializerTestCase
from .serializers import PatientAssessmentSerializer


class PatientAssessmentSerializerTest(BaseSerializerTestCase):

    serializer_class = PatientAssessmentSerializer

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="testuser")
        self.patient = Patient.objects.create(
            assigned_clinician=self.user,
            full_name="John Doe",
            gender=GenderChoices.MALE,
            birthdate=date(1990, 6, 15),
            phone="1234567890",
            address="Cn432423432"
        )
        self.valid_data = {
            'patient': self.patient.id,
            'type': 'Initial',
            'date': '2024-02-02',
            'score': 85,
            'qna_rounds': [{'question': 'How are you?', 'answer': 'Good'}]
        }

    def _test_valid_data_with_context(self):
        request = self.factory.post('/some-url/')
        request.user = self.user

        self._test_valid_data(request_context=request)

    def _test_invalid_data_part_with_context(self, invalid_data_part: dict):
        request = self.factory.post('/some-url/')
        request.user = self.user

        self._test_invalid_data_part(invalid_data_part, request_context=request)

    def test_valid_data(self):
        self._test_valid_data_with_context()

    def test_invalid_date(self):
        invalid_date_future = (timezone.now().date() + timedelta(days=1)).isoformat()
        invalid_date_before_born = (self.patient.birthdate - timedelta(1)).isoformat()

        key = 'date'

        self._test_invalid_data_part_with_context({key: invalid_date_future})
        self._test_invalid_data_part_with_context({key: invalid_date_before_born})

    def test_invalid_type(self):
        invalid_type_format = '!nval*d 5ype'

        self._test_invalid_data_part_with_context({'type': invalid_type_format})

    def test_invalid_score(self):
        invalid_score_gt_max = 101

        self._test_invalid_data_part_with_context({'score': invalid_score_gt_max})

    def test_invalid_qna_rounds(self):
        invalid_qna_none = None
        invalid_qna_empty_list = []
        invalid_qna_empty_dict = {}
        invalid_qna_no_question = [{'question': None, 'answer': 'Some answer'}]

        key = 'qna_rounds'

        self._test_invalid_data_part_with_context({key: invalid_qna_none})
        self._test_invalid_data_part_with_context({key: invalid_qna_empty_list})
        self._test_invalid_data_part_with_context({key: invalid_qna_empty_dict})
        self._test_invalid_data_part_with_context({key: invalid_qna_no_question})
