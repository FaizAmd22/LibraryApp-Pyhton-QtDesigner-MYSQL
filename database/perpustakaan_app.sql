-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 08 Nov 2024 pada 04.35
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan_app`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `anggota`
--

CREATE TABLE `anggota` (
  `id_anggota` varchar(25) NOT NULL,
  `nama_anggota` varchar(100) NOT NULL,
  `jenis_kelamin` varchar(15) NOT NULL,
  `alamat` varchar(20) NOT NULL,
  `no_hp` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `anggota`
--

INSERT INTO `anggota` (`id_anggota`, `nama_anggota`, `jenis_kelamin`, `alamat`, `no_hp`, `email`, `is_delete`) VALUES
('2', 'orang2', 'Laki-laki', 'aslkdhalskjdlka', '0298130928301982', 'test@mail.com', 1),
('3', 'test03', 'Laki-laki', 'asdasdwdasdas', '2312312312312', 'mail03@mail.com', 1),
('MBR15002', 'aefasdasda', 'Perempuan', 'sdasdasdasd', '324342342342342', 'mail@mail.com', 1),
('MBR15269', 'Christ John', 'Laki-laki', 'Ciledug', '012934567891', 'jonkris@mail.com', 0),
('MBR6348', 'wsdasdasda', 'Perempuan', 'dsadasasfa', '2132121231', 'mail@mail.c', 1),
('MBR81087', 'akjsbdkajbsd', 'Perempuan', 'sdasdasdasdas', '209173029703912', 'email@mail.co', 1),
('MBR83805', 'Anggota Baru', 'Perempuan', 'Heaven', '01111111111111111', 'angel@gmail.com', 0),
('MBR89666', 'Ujang Karbu', 'Laki-laki', 'Kab. Bogor', '0811111111111', 'ujang@gmail.com', 0),
('MBR99437', 'Mamang Racing', 'Laki-laki', 'Depok Pride', '08213625317622', 'racingspeed@gamil.com', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku`
--

CREATE TABLE `buku` (
  `isbn` varchar(20) NOT NULL,
  `nama_genre` varchar(255) NOT NULL,
  `nama_penulis` varchar(255) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `penerbit` varchar(100) NOT NULL,
  `tanggal_publikasi` date NOT NULL,
  `jumlah_stok` int(11) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `buku`
--

INSERT INTO `buku` (`isbn`, `nama_genre`, `nama_penulis`, `judul`, `penerbit`, `tanggal_publikasi`, `jumlah_stok`, `is_delete`) VALUES
('28371t82732', 'rterawaw', 'testtt', 'testt', 'asdaweawea', '2000-01-01', 12, 1),
('9786020631653', 'Misteri', 'Sir Arthur Conan Doyle', 'Sherlock Holmes - A Study In Scarlet', 'Gramedia Pustaka Utama', '2019-07-29', 34, 0),
('9786022203049', 'Fiksi', 'J. S Khairen', 'Kami (Bukan) Sarjana Kertas', 'Kawah Media', '2019-02-14', 44, 0),
('9789797809492', 'Horor', 'Kisah Tanah Jawa', 'Kisah Tanah Jawa : Pocong Gundul', 'Kawah Media', '2019-12-21', 2, 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `genre`
--

CREATE TABLE `genre` (
  `id_genre` int(25) NOT NULL,
  `nama_genre` varchar(255) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `genre`
--

INSERT INTO `genre` (`id_genre`, `nama_genre`, `is_delete`) VALUES
(1, 'Algoritma dan Pemograman', 0),
(2, 'Fiksi', 0),
(3, 'Misteri', 0),
(4, 'Horor', 0),
(5, 'rterawaw', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `peminjaman_buku`
--

CREATE TABLE `peminjaman_buku` (
  `id_peminjaman` varchar(11) NOT NULL,
  `nama_anggota` varchar(255) NOT NULL,
  `judul_buku` varchar(255) NOT NULL,
  `tanggal_peminjaman` date NOT NULL,
  `tanggal_untuk_pengembalian` date NOT NULL,
  `tanggal_pengembalian` date DEFAULT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `peminjaman_buku`
--

INSERT INTO `peminjaman_buku` (`id_peminjaman`, `nama_anggota`, `judul_buku`, `tanggal_peminjaman`, `tanggal_untuk_pengembalian`, `tanggal_pengembalian`, `is_delete`) VALUES
('19085282', 'Ujang Karbu', 'Kisah Tanah Jawa : Pocong Gundul', '2024-11-08', '2024-11-15', '2024-11-08', 0),
('29494173', 'Christ John', 'Kisah Tanah Jawa : Pocong Gundul', '2024-11-08', '2024-11-15', '2024-11-08', 0),
('50037508', 'Anggota Baru', 'Kisah Tanah Jawa : Pocong Gundul', '2024-11-08', '2024-11-15', '2024-11-08', 0),
('51354152', 'Mamang Racing', 'Sherlock Holmes - A Study In Scarlet', '2024-11-08', '2024-11-15', '2024-11-08', 0),
('63959375', 'Mamang Racing', 'Kami (Bukan) Sarjana Kertas', '2024-11-08', '2024-11-15', NULL, 0),
('71026458', 'Ujang Karbu', 'Sherlock Holmes - A Study In Scarlet', '2024-11-07', '2024-11-14', '2024-11-14', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `penulis`
--

CREATE TABLE `penulis` (
  `id_penulis` int(25) NOT NULL,
  `nama_penulis` varchar(255) NOT NULL,
  `is_delete` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `penulis`
--

INSERT INTO `penulis` (`id_penulis`, `nama_penulis`, `is_delete`) VALUES
(1, 'Arik Kurniawati', 0),
(2, 'J. S Khairen', 0),
(3, 'Sir Arthur Conan Doyle', 0),
(4, 'Sir Arthur Conan D', 0),
(5, 'Kisah Tanah Jawa', 0),
(6, 'testtt', 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id_user` int(25) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id_user`, `nama`, `username`, `password`) VALUES
(1, 'admin', 'admin', 'c93ccd78b2076528346216b3b2f701e6');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`id_anggota`),
  ADD UNIQUE KEY `nama_anggota` (`nama_anggota`);

--
-- Indeks untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`isbn`),
  ADD UNIQUE KEY `judul` (`judul`),
  ADD KEY `id_genre` (`nama_genre`,`nama_penulis`),
  ADD KEY `nama_penulis` (`nama_penulis`);

--
-- Indeks untuk tabel `genre`
--
ALTER TABLE `genre`
  ADD PRIMARY KEY (`id_genre`),
  ADD UNIQUE KEY `nama_genre` (`nama_genre`);

--
-- Indeks untuk tabel `peminjaman_buku`
--
ALTER TABLE `peminjaman_buku`
  ADD PRIMARY KEY (`id_peminjaman`),
  ADD KEY `id_anggota` (`nama_anggota`),
  ADD KEY `judul_buku` (`judul_buku`),
  ADD KEY `nama_anggota` (`nama_anggota`);

--
-- Indeks untuk tabel `penulis`
--
ALTER TABLE `penulis`
  ADD PRIMARY KEY (`id_penulis`),
  ADD UNIQUE KEY `nama_penulis` (`nama_penulis`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `genre`
--
ALTER TABLE `genre`
  MODIFY `id_genre` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `penulis`
--
ALTER TABLE `penulis`
  MODIFY `id_penulis` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD CONSTRAINT `buku_ibfk_1` FOREIGN KEY (`nama_genre`) REFERENCES `genre` (`nama_genre`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `buku_ibfk_2` FOREIGN KEY (`nama_penulis`) REFERENCES `penulis` (`nama_penulis`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Ketidakleluasaan untuk tabel `peminjaman_buku`
--
ALTER TABLE `peminjaman_buku`
  ADD CONSTRAINT `peminjaman_buku_ibfk_1` FOREIGN KEY (`judul_buku`) REFERENCES `buku` (`judul`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `peminjaman_buku_ibfk_2` FOREIGN KEY (`nama_anggota`) REFERENCES `anggota` (`nama_anggota`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
