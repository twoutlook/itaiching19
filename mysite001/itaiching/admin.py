from django.contrib import admin

# Register your models here.

from .models import TaichiStyle
from .models import TaichiSet
from .models import TaichiMove

# only show def __str__(self):
# admin.site.register(TaichiStyle)
# admin.site.register(TaichiSet)
# admin.site.register(TaichiMove)

# to show selected fields
class TaichiStyleAdmin(admin.ModelAdmin):
    list_display=['code','title','description']
    ordering = ['code']
admin.site.register(TaichiStyle,TaichiStyleAdmin)

class TaichiSetAdmin(admin.ModelAdmin):
    # list_display=['taichistyle','title','description']
    list_display=['taichistyle','title','id']

    ordering = ['taichistyle','title']
admin.site.register(TaichiSet,TaichiSetAdmin)


class TaichiMoveAdmin(admin.ModelAdmin):
    list_display=['stylenum', 'setnum','taichiset','movenum','mnemonic','title','description']
    ordering = ['stylenum','taichiset', 'setnum', 'movenum']
admin.site.register(TaichiMove,TaichiMoveAdmin)
