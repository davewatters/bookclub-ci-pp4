from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author= models.CharField(max_length=60, unique=True)
    publisher = models.CharField(max_length=40, blank=True)
    year_published = models.CharField(max_length=4, blank=True)
    synopsis = models.TextField(blank=True)
    cover_image = CloudinaryField('image', default='placeholder')
    members_rating = models.PositiveSmallIntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def has_been_read(self):
        return Meetup.objects.get(book1=self.id)

    @property
    def long_title(self):
        return (self.title +' by ' +self.author)


class Meetup(models.Model):

    MEETUP_STATUS = (
        (0, 'Scheduled'),
        (1, 'Finished'),
        (2, 'Cancelled')
    )

    title = models.CharField(max_length=40,unique=True)
    meetup_date = models.DateField(blank=False)
    book1 = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book1')
    # book2 = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book2')
    details = models.TextField(blank=False)
    status = models.IntegerField(choices=MEETUP_STATUS, default=0)
    slug = models.SlugField(max_length=40, unique=True)

    class Meta:
        ordering = ["-meetup_date"]

    @property
    def meetup_title(self):
         return ('Meetup '+str(self.id) + self.meetup_date.strftime(': %B, %Y'))

    def __str__(self):
        return self.meetup_title

    @property
    def book1_detail(self):
        return Book.objects.get(id=self.book1_id)


    # def save(self, *args, **kwargs):
    #     self.title = self.meetup_title
    #     self.slug = slugify(self.meetup_title)
    #     super(Meetup, self).save(*args, **kwargs)
