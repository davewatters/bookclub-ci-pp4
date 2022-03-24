from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author= models.CharField(max_length=60, unique=True)
    publisher = models.CharField(max_length=40)
    year_pubished = models.PositiveSmallIntegerField(blank=True, null=True)
    synopsis = models.TextField(blank=True)
    # cover_image = 'placeholder'
    members_rating = models.PositiveSmallIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User)

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return self.title


class Meetup(models.Model):

    MEETUP_STATUS = (
        (0, 'Scheduled'),
        (1, 'Finished'),
        (2, 'Cancelled')
    )

    meetup_date = models.DateTimeField(blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    book1_id = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book1')
    book2_id = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book2')
    details = models.TextField(blank=False)
    status = models.IntegerField(choices=MEETUP_STATUS, default=0)

    def __str__(self):
        return (self.meetup_date.strftime('%B'))
