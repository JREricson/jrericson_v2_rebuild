from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Project(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        # # verbose_name=_("project title"),
        # help_text=_("format: required, max-100"),
    )

    description = models.TextField(
        unique=False,
        null=False,
        # blank=False,
        # verbose_name=_("project description"),
        # help_text=_("format: required"),
    )

    description_short = models.TextField(
        max_length=1000, unique=False, null=False, default="<Not provided>"
    )
    concepts = models.TextField(
        max_length=1000,
        unique=False,
        null=True,
        blank=True,
    )

    technology = models.TextField(
        max_length=1000,
        unique=False,
        null=True,
        blank=True,
    )
    rank = models.FloatField(
        default=5, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )

    github = models.URLField(
        max_length=150,
        unique=False,
        null=False,
        blank=True,
        # verbose_name=_("github url"),
        # help_text=_("format: required"),
    )

    website = models.URLField(
        max_length=150,
        unique=False,
        null=False,
        blank=True,
        # verbose_name=_("project website"),
        # help_text=_("format: required"),
    )

    img_url = models.URLField(
        max_length=150,
        unique=False,
        null=False,
        blank=True,
        # verbose_name=_("project image url"),
        # help_text=_("format: required"),
    )

    featured = models.BooleanField(
        default=True,
        null=False,
        blank=False,
        # verbose_name=_("project image url"),
        # help_text=_("format: required"),
    )

    date_posted = models.DateTimeField(default=timezone.now)

    date_updated = models.DateTimeField(auto_now=True)

    # tags = ArrayField(models.CharField(max_length=35, blank=True))

    # date_posted = models.DateTimeField(default=timezone.now)
    # deletes all user's posts with CASCADE
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["title"]

    # added to make easier to understand
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("project-detail", kwargs={"pk": self.pk})


# get tags list before
# if removed one of tags
# if tag has no other refs
# delete tag


# @receiver(post_save, sender=Project,
# dispatch_uid="delete_tags_with_no_project")
# def delete_tags_with_no_project(sender, instance, **kwargs):

# for each tag
# check if tag has other references, if not delete tag
# if not Server.objects.filter(contact=instance.contact):
#     instance.contact.delete()

# @receiver(post_delete, sender=Project,
#  dispatch_uid="delete_tags_with_no_project")
