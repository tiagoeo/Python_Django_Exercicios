# Generated by Django 5.1.3 on 2024-11-18 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_produto", models.CharField(max_length=100)),
                ("preco_produto", models.DecimalField(decimal_places=2, max_digits=8)),
                ("descricao_produto", models.TextField()),
            ],
        ),
    ]