from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length=100)
    pembuat = models.CharField(max_length=100)
    jenis = models.CharField(max_length=100)
    spesifikasi = models.TextField()

    def __str__(self):
        return self.nama_barang

    class Meta:
        verbose_name_plural = "Daftar Barang"

STATUS_BARANG=(
    (1, 'Aktif'),
    (2, 'Rusak'),
    (3, 'Hilang'),
    (4, 'Dilelang'),
)

class Inventaris(models.Model):
    barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    no_inventaris = models.CharField(max_length=50)
    tanggal_pembelian = models.DateField()
    petugas_pengadaan = models.CharField(max_length=100)
    harga_pembelian = models.BigIntegerField()
    lokasi = models.CharField(max_length=100)
    tanggal_maintenance_terakhir = models.DateField(blank=True, null=True)
    nama_petugas_maintenance = models.CharField(max_length=100, null=True, blank=True)
    status_barang = models.IntegerField(choices=STATUS_BARANG, default=1)

    def __str__(self):
        return self.no_inventaris

    class Meta:
        verbose_name_plural = "Daftar Inventaris"
