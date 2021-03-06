import json
import pytest
import logging
from unittest import TestCase
from django.test import Client
from django.urls import reverse
from companies.models import Company

logger = logging.getLogger("CORONA_LOGS")


@pytest.mark.django_db
class BasicCompanyAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass


class TestGetCompanies(BasicCompanyAPITestCase):
    def test_zero_companies_should_return_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        test_company = Company.objects.create(name="Hugos")
        response = self.client.get(self.companies_url)
        print(response.content)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), test_company.name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")
        test_company.delete()


class TestPostCompanies(BasicCompanyAPITestCase):
    def test_create_company_without_arguments_should_fail(self) -> None:
        response = self.client.post(path=self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_existing_company_should_fail(self) -> None:
        Company.objects.create(name="Hugos")
        response = self.client.post(path=self.companies_url, data={"name": "Hugos"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),
            {"name": ["company with this name already exists."]},
        )

    def test_create_company_with_only_name_all_fields_should_be_default(self) -> None:
        response = self.client.post(path=self.companies_url, data={"name": "Hugos"})
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), "Hugos")
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

    def test_create_company_with_layoffs_status_should_succeed(self) -> None:
        response = self.client.post(
            path=self.companies_url, data={"name": "Hugos", "status": "Hiring Freeze"}
        )
        self.assertEqual(response.status_code, 201)
        response_content = json.loads(response.content)
        self.assertEqual(response_content.get("name"), "Hugos")
        self.assertEqual(response_content.get("status"), "Hiring Freeze")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

    def test_create_company_with_wrong_status_should_fail(self) -> None:
        response = self.client.post(
            path=self.companies_url, data={"name": "Hugos", "status": "WrongStatus"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("WrongStatus", str(response.content))
        self.assertIn("is not a valid choice.", str(response.content))


class TestDummyInfo(TestCase):
    @pytest.mark.xfail
    def test_should_be_ok_if_fails(self) -> None:
        self.assertEqual(1, 2)

    @pytest.mark.skip
    def test_should_be_skipped(self) -> None:
        self.assertEqual(1, 2)

    def raise_covid19_exception(self) -> None:
        raise ValueError("CoronaVirus Exception")

    def test_raise_covid19_exception_should_pass(self) -> None:
        with pytest.raises(ValueError) as e:
            self.raise_covid19_exception()
        assert "CoronaVirus Exception" == str(e.value)


## Other Test


def function_that_logs_something() -> None:
    try:
        raise ValueError("Logging TEST")
    except ValueError as e:
        logger.warning(f"ERROR: {e}")


def test_logged_warning_level(caplog) -> None:
    function_that_logs_something()
    assert "ERROR: Logging TEST" in caplog.text


def test_logged_info_level(caplog) -> None:
    with caplog.at_level(logging.INFO):
        logger.info("I am logging info level")
        assert "I am logging info level" in caplog.text
