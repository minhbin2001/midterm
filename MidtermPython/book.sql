-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 26, 2021 at 07:42 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `bId` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `Name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `Price` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `Year` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `Publisher` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `Author` varchar(225) COLLATE utf8_unicode_ci NOT NULL,
  `Quantity` varchar(225) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`bId`, `Name`, `Price`, `Year`, `Publisher`, `Author`, `Quantity`) VALUES
('1', 'Sách Giáo Khoa Toán Lớp 9 - Tập 1', '7000', '2018', 'Bộ GIáo Dục và Đào Tạo', 'Bộ GIáo Dục và Đào Tạo', '5000'),
('2', 'Harry Potter Và Đứa Trẻ Bị Nguyền Rủa: Phần Một Và Hai', '128000', '2017', 'NXB trẻ', 'Dr. Devin Dennie, Jack Thorne, John Tiffany', '1000');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
