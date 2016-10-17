from django.db import models

# Create your models here.

class TaichiStyle(models.Model):
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    code = models.CharField(default="x",max_length=6,verbose_name="編碼")
    title = models.CharField(max_length=200,verbose_name="線路名稱")
    description = models.CharField(max_length=200,verbose_name="說明")
    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "線路"
        verbose_name_plural = "(1)線路"

    # Set is a keyword
class TaichiSet(models.Model):
    taichistyle = models.ForeignKey(TaichiStyle, on_delete=models.CASCADE,verbose_name="線路名稱")
    # num = models.IntegerField(default=0,verbose_name="第幾式")
    title = models.CharField(max_length=200,verbose_name="招式名稱")
    description = models.CharField(max_length=200,verbose_name="招式說明")
    mynote = models.CharField(default=".", max_length=600,verbose_name="我的筆記")
   # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "(2)招式"
        verbose_name_plural = "(2)招式"

class TaichiMove(models.Model):
    stylenum= models.IntegerField(default=0,verbose_name="幾式")
    taichiset = models.ForeignKey(TaichiSet, on_delete=models.CASCADE)
    setnum = models.IntegerField(default=0,verbose_name="第幾式")

    movenum = models.IntegerField(default=0,verbose_name="第幾動")
    mnemonic = models.CharField(default=".",max_length=20,verbose_name="助憶")
    title = models.CharField(max_length=200,verbose_name="動作口訣")
    description = models.CharField(max_length=200,verbose_name="動作要求")
    mynote = models.CharField(default=".", max_length=600,verbose_name="我的筆記")

    # remarks = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "(3)動作"
        verbose_name_plural = "(3)動作"
