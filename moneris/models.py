from django.db import models

# Create your models here.


class Moneris(models.Model):
    status = (
        ('test', 'Test'),
        ('prod', 'Prod')
    )
    name = models.CharField(max_length=100, unique=True)
    ps_store_id = models.CharField(max_length=100, null=False, blank=False)
    hpp_key = models.CharField(max_length=100, null=False, blank=False)
    access_token = models.CharField(max_length=100, null=True, blank=True)
    api_username = models.CharField(max_length=100, null=True, blank=True)
    api_password = models.CharField(max_length=100, null=True, blank=True)
    environment = models.CharField(max_length=10, choices=status, default='test')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def _get_moneris_urls(self, environment):
        """ Moneris URLS """
        if environment == 'prod':
            return {
                'moneris_form_url': 'https://www3.moneris.com/HPPDP/index.php',
                'moneris_auth_url': 'https://www3.moneris.com/HPPDP/verifyTxn.php',
            }
        else:
            return {
                'moneris_form_url': 'https://esqa.moneris.com/HPPDP/index.php',
                'moneris_auth_url': 'https://esqa.moneris.com/HPPDP/verifyTxn.php',
            }