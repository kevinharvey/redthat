from rest_framework.test import APITestCase, APIClient

from model_mommy import mommy

from .models import Submission


class SubmissionsEndpointTestCase(APITestCase):

    def test_submission_detail(self):
        """
        Test the detail endpoint for Submissions
        """
        submission = mommy.make(Submission)
        client = APIClient()

        response = client.get(f'/submissions/{submission.id}/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'url': f'http://testserver/submissions/{submission.id}/',
            'title': submission.title,
            'external_link': submission.external_link,
            'upvotes': submission.upvotes,
            'downvotes': submission.downvotes
        })
