-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2021 at 10:49 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blogsite`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_name` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_name`, `first_name`, `last_name`, `password`, `id`) VALUES
('pp', 'oo', 'pp', 'oo', 4),
('ll', 'lll', 'kk', '$5$rounds=535000$l16H2l0GeJFdQ2ZG$uGeSzVTvnHnvHxoOd9vDVSf4NgO9yvgLOSFuFq5hVd6', 5),
('pp', 'nnnnnnnnnn', 'nnn', '$5$rounds=535000$Von/AD5PLeZGpPas$WFzagi1N4lWzIIOj7Zk9Lsp9wVqT3DyqN4S/bCB5sB8', 6),
('nn', 'nn', 'lllllllllllll', '$5$rounds=535000$to6HdirlRyRP7fyH$kFargNEwiIMajsi4rrZPc3/UBl5aErGhTcpL1QPMIpA', 7),
('pp', 'll', 'kk', '$5$rounds=535000$lqgE2osKkgXaaj6Y$uyEwSjMS56hLGqbiQDU6VgXAGfqjylRCwJrXUAmQnd3', 8),
('l', 'k', 'k', '$5$rounds=535000$jM.mri9c6L939NK8$jmsnbaXRHLwRFU0H/4z3FGbzyUtz6RSobWzWC9o3Ik8', 9),
('kk', 'kll', 'k', '$5$rounds=535000$xUAYjkjzBbiJIbsH$ySfz6th/Yz91FtHGx0g3rhSsoFLyJyZBCAKKESYBTz9', 10),
('k', 'k', 'k', '$5$rounds=535000$gOjexy0f2r/SoPCQ$9LA40KPHBfMouCmQCgUqG4TKauK58m9C0Z2A6bKFMU5', 11),
('h', 'h', 'h', '$5$rounds=535000$nAyKewAtnmyD8hP8$Ss.28hpRM5.0xb3O.EkGff6SI6pQgbypQuPmStRFaR/', 12);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
