from django.db import models

from django.utils import timezone # for is_new function


class ProductSizeModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'size'
        verbose_name_plural = 'sizes'


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductColorModel(models.Model):
    code = models.CharField(max_length=7)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'color'
        verbose_name_plural = 'colors'


class ProductTagModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class ProductBrandModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class ProductModel(models.Model):
    title = models.CharField(max_length=85)
    short_description = models.TextField()
    long_description = models.TextField()
    price = models.FloatField()
    real_price = models.FloatField(default=0)
    discount = models.PositiveSmallIntegerField(default=0)  # 20%
    main_image = models.ImageField(upload_to='products/')
    tags = models.ManyToManyField(ProductTagModel, related_name='products')
    colors = models.ManyToManyField(ProductColorModel, related_name='products')
    size = models.ManyToManyField(ProductSizeModel, related_name='products')
    sku_id = models.IntegerField()
    brand = models.ForeignKey(ProductBrandModel, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    # def real_price(self):
    #     if self.discount:
    #         return self.price - (self.price * self.discount) / 100
    #     else:
    #         return self.price

    def is_discount(self):
        return self.discount != 0

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 3

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ('-id',)

