from django.contrib import admin

# Register your models here.

from .models import TaichiStyle
from .models import TaichiSet
from .models import TaichiMove



from import_export import resources
# from core.models import Book
#
# class BookResource(resources.ModelResource):
#
#     class Meta:
#         model = Book
from import_export.admin import ImportExportModelAdmin

# class BookAdmin(ImportExportModelAdmin):
#     resource_class = BookResource

from import_export import resources
class TaichiMoveResource(resources.ModelResource):
    class Meta:
        model = TaichiMove

class TaichiMoveAdmin(ImportExportModelAdmin):
    resource_class = TaichiMoveResource
admin.site.register(TaichiMove,TaichiMoveAdmin)
# class TaichiMoveAdmin(admin.ModelAdmin):
#     list_display=['stylenum', 'setnum','movenum','pagenum','mnemonic','title','description']
#     ordering = ['-stylenum', '-setnum', '-movenum']
# admin.site.register(TaichiMove,TaichiMoveAdmin)




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
