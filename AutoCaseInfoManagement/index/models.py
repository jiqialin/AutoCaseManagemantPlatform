from django.db import models


# Create your models here.


class BaseModelTable(models.Model):
    id = models.AutoField("id", primary_key=True)

    create_time = models.DateTimeField(null=True, verbose_name='创建时间', auto_now_add=True)
    modify_time = models.DateTimeField(null=True, verbose_name='修改时间', auto_now=True)
    is_deleted = models.IntegerField('0：未删除 1：已删除', null=True, default=0)

    class Meta:
        abstract = True  # 定义抽象models class
        ordering = ['-create_time']


class Department(BaseModelTable):
    name = models.CharField("部门名", max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部门表"
        db_table = 'department'


class BusinessLine(BaseModelTable):
    lineName = models.CharField('业务线名', max_length=50, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.lineName

    class Meta:
        verbose_name = "业务线表"
        db_table = 'business_line'


class Group(BaseModelTable):
    groupName = models.CharField('垂直小组名', max_length=50, null=True)
    businessLine = models.ForeignKey(BusinessLine, on_delete=models.CASCADE)

    def __str__(self):
        return self.groupName

    class Meta:
        verbose_name = "垂直小组表"
        db_table = 'business_group'


class Config(BaseModelTable):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    moduleName = models.CharField('模块名称', max_length=20, null=True)
    gitAddress = models.URLField('git地址', null=True)
    caseType = models.IntegerField('用例类型')
    creator = models.CharField('创建人', max_length=20, null=True)
    modifier = models.CharField('修改人', max_length=20, null=True)

    def __str__(self):
        return self.moduleName

    class Meta:
        verbose_name = "配置信息"
        db_table = 'git_config'


from django.db import connection


class BusinessManager(models.Manager):
    """
        测试用例管理器
        过滤状态为 0 启用的用例信息展示
    """
    id = 1
    status = 0

    def get_queryset(self):
        return super(BusinessManager, self).get_queryset().filter(status=0)

    def ownCustomSql(self):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE case_info SET status = 1 WHERE id = %s", [self.id, ])
            cursor.execute("SELECT * FROM case_info WHERE status = %s", [self.status, ])
            row = cursor.fetchone()
        return row


class CaseInfo(BaseModelTable):
    STATUS_CHOICES = [(0, '正常'), (1, '废弃'), ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    moduleName = models.CharField('模块名称', max_length=20, null=True)
    caseName = models.CharField('用例名称', max_length=50, null=True)
    caseType = models.IntegerField('用例类型')
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=0)
    casePath = models.CharField('用例路径', max_length=50, null=True)
    modifier = models.CharField('修改人', max_length=20, null=True)
    apiName = models.CharField('接口名称', max_length=50, null=True)
    excelId = models.IntegerField(null=True)
    serverName = models.CharField('服务名', max_length=50, null=True)

    objects = models.Manager()
    businessData = BusinessManager()

    def __str__(self):
        return self.caseName

    class Meta:
        verbose_name = "用例信息"
        db_table = 'case_info'






