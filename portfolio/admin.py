from django.contrib import admin
from .models import Testimonial, Shopping, Ask, Subscriber, Newsletter, Course

# Register your models here.

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Testimonial)
admin.site.register(Shopping)
admin.site.register(Ask)
admin.site.register(Subscriber)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Course)



