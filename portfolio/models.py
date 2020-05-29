from django.db import models
import datetime
from django.utils import timezone
from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.

  
class Course(models.Model):
    Course_Topic = models.CharField(max_length=200)
    Book = models.FileField(upload_to="documents/", null=True, blank=True)
    Video = models.CharField(max_length=100, null=True, blank=True)   
    Uploaded_by = models.CharField(max_length=1000)
    Date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.Course_Topic

class Testimonial(models.Model):
    Name = models.CharField(max_length = 50)
    Testimonial = models.TextField(max_length=500)
    Date = models.DateTimeField(default=timezone.now)
    Approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = False
        self.save()

    def __str__(self):
        return self.Name


class Shopping(models.Model):
    STATUS = (
        ('.all', ('All')),
       ('.computers', ('Computers')),
       ('.phones', ('Phones')),
       ('.Cameras', ('Cameras')),
    )
    Title = models.CharField(max_length=50)
    Image = models.ImageField(upload_to = 'images/', null =True, blank = True)
    Description = models.TextField()
    Price = models.IntegerField()
    Brand = models.CharField(max_length=50, choices = STATUS, default='.all')
    
    def __str__(self):
        return self.Title

class Ask(models.Model):
    Subject = models.CharField(max_length=200)
    Statement = models.TextField()
    Approved = models.BooleanField(default=False)

    def approve(self):
        self.Approved = False
        self.save()

    def __str__(self):
        return self.Subject

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"

class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    Message = models.TextField(null=True)
    contents = models.FileField(upload_to='uploaded_newsletters/', blank=True, default='upload')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject=self.subject,
                    html_content=contents + (
                        '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.conf_num))
            sg.send(message)

