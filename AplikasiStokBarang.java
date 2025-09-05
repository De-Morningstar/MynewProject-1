import java.util.ArrayList;
import java.util.Scanner;

class Barang {
    private String kodeBarang;
    private String namaBarang;
    private int stok;

    public Barang(String kodeBarang, String namaBarang, int stok){
        this.kodeBarang = kodeBarang;
        this.namaBarang = namaBarang;
        this.stok = stok;
    }

    public String getKodeBarang() {
        return kodeBarang;
    }

    public String getNamaBarang() {
        return namaBarang;
    }

    public int getStok() {
        return stok;
    }

    public void setStok(int stok) {
        this.stok = stok;
    }
}


public class AplikasiStokBarang{
    private ArrayList<Barang> daftarBarang;
    private Scanner scanner;

    public AplikasiStokBarang(){
        daftarBarang = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    public void tambahBarang(){
        System.out.println("Masukkan kode barang : ");
        String kodeBarang = scanner.nextLine();
        System.out.println("Masukkan nama barang : ");
        String namaBarang = scanner.nextLine();
        System.out.println("Masukkan stok : ");
        int stok = scanner.nextInt();
        scanner.nextLine();

        Barang barang = new Barang(kodeBarang,namaBarang,stok);
        daftarBarang.add(barang);
        System.out.println("Barang berhasil ditambahkan!");
    }

    public void lihatBarang(){
        if (daftarBarang.isEmpty()){
            System.out.println("Belum ada barang!");
        }else {
            for (Barang barang : daftarBarang){
                System.out.println("Kode barang: " + barang.getKodeBarang());
                System.out.println("Nama barang: " + barang.getNamaBarang());
                System.out.println("Stok: " + barang.getStok());
                System.out.println();
            }
        }
    }

    public void updateStok(){
        System.out.println("Masukkan kode barang : ");
        String kodeBarang = scanner.nextLine();

        for (Barang barang : daftarBarang){
            if (barang.getKodeBarang().equals(kodeBarang)){
                System.out.println("Masukkan stok baru: ");
                int stokBaru = scanner.nextInt();
                scanner.nextLine();
                barang.setStok(stokBaru);
                System.out.println("Stok berhasil diupdate!");
                return;
            }
        }
        System.out.println("BARANG TIDAK DITEMUKAN !");
    }

    public void hapusBarang(){
        System.out.println("Masukkan kode barang: ");
        String kodeBarang =scanner.nextLine();

        for (Barang barang : daftarBarang){
            if (barang.getKodeBarang().equals(kodeBarang)){
                daftarBarang.remove(barang);
                System.out.println("Barang berhasil dihapus !");
                return;
            }
        }
        System.out.println("BARANG TIDAK DITEMUKAN!");
    }

    public void run(){
        while (true){
            System.out.println(">>> APLIKASI STOK BARANG <<<");
            System.out.println("1. Tambah Barang");
            System.out.println("2. Lihat Barang");
            System.out.println("3. Update Stok");
            System.out.println("4. Hapus Barang");
            System.out.println("5. Keluar");
            System.out.println("Pilih menu :");
            int pilihan = scanner.nextInt();
            scanner.nextLine();

            switch (pilihan){
                case 1:
                    tambahBarang();
                    break;
                case 2:
                    lihatBarang();
                    break;
                case 3:
                    updateStok();
                    break;
                case 4:
                    hapusBarang();
                    break;
                case 5:
                    System.out.println("Terima kasih!");
                    return;
                default:
                    System.out.println("Pilihan Tidak Valid!");
            }
        }
    }

    public static void main(String[] args) {
        AplikasiStokBarang aplikasi = new AplikasiStokBarang();
        aplikasi.run();
    }
}