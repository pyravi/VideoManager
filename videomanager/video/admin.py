from django.contrib import admin
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from .models import TitleManager,VideoManager

# Register your models here.
class TitleAdminManagerAdmin(DraggableMPTTAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20
    exclude = ("slug",)
 


class VideoManagerAdmin(admin.ModelAdmin):
    list_display = ["title","video_description", "parent_title", "videofile" ,"timestamp"]
    search_fields= ("videofile",)
    exclude = ("slug",)

admin.site.register(TitleManager, TitleAdminManagerAdmin)
admin.site.register(VideoManager, VideoManagerAdmin)
