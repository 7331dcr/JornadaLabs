from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"(id: {self.id}) (name: {self.name}) (created_on: {self.created_on}"

class Operation(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE, related_name="operations")
    source_currency = models.CharField(max_length=255, blank=False, null=False)
    target_currency = models.CharField(max_length=255, blank=False, null=False)
    source_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    converted_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=False)
    fee = models.DecimalField(max_digits=14, decimal_places=2, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"""(id: {self.id}) (client: {self.client.name})
        (source: {self.source_currency}) (target: {self.target_currency}) (amount: {self.source_currency})
        (converted: {self.converted_amount}) (fee: {self.fee}) (created on: {self.created_on})"""