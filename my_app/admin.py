from django.contrib import admin
from my_app.models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

@admin.action(description="Email Sending")
def email_sending(self, request, queryset):
    content = ContentData.objects.get(status="SELECTED")
    for obj in queryset:
        send_mail(
            content.title,
            content.content,
            settings.EMAIL_HOST_USER,
            [obj.email],
            fail_silently=False,
        )
        messages.success(request, f'{request}')

@admin.action(description="Content Select")
def content_selected(self, request, queryset):
    content = ContentData.objects.all()
    for c in content:
        c.status = "UNSELECTED"
        c.save()
    updated = queryset.update(status="SELECTED")
    messages.success(request, 'Success ')
    
class AdminHotel(admin.ModelAdmin):
    fields = ['name','email','phone','address']
    list_display = ['id','name','email','phone','address','created_at']
    ordering = ['name']
    actions = [email_sending]

class AdminContent(admin.ModelAdmin):
    fields = ['title','content']
    list_display = ['id','title','content','status','created_at']
    ordering = ['title']
    actions = [content_selected]
    

admin.site.register(HotelData,AdminHotel)
# admin.site.disable_action("delete_selected")
admin.site.register(ContentData,AdminContent)