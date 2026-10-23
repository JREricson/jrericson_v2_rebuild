from django.test import Client, TestCase
from django.urls import reverse

from .models import Project


class ProjectModelTests(TestCase):
    def test_str_returns_title(self):
        project = Project.objects.create(
            title="Example Project",
            description="A longer description",
            description_short="Short description",
            github="",
            website="",
            img_url="",
        )
        self.assertEqual(str(project), "Example Project")


class PortfolioViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            title="Sample Project",
            description="## Hello\n\nProject body text.",
            description_short="A short blurb",
            github="https://github.com/example/repo",
            website="",
            img_url="",
            rank=8,
            featured=True,
        )

    def test_about_returns_200(self):
        response = self.client.get(reverse("portfolio:about"))
        self.assertEqual(response.status_code, 200)

    def test_projects_list_returns_200_and_shows_title(self):
        response = self.client.get(reverse("portfolio:projects"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Project")

    def test_project_detail_returns_200_and_renders_markdown(self):
        response = self.client.get(
            reverse("portfolio:project", kwargs={"pk": self.project.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sample Project")
        self.assertContains(response, "Hello")

    def test_contact_redirects_to_linkedin(self):
        response = self.client.get(reverse("portfolio:contact"))
        self.assertEqual(response.status_code, 302)
        self.assertIn("linkedin.com", response["Location"])
