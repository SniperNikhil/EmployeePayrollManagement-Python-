-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2022 at 03:35 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ems`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_salary`
--

CREATE TABLE `emp_salary` (
  `e_id` int(11) NOT NULL,
  `Designation` text NOT NULL,
  `name` text NOT NULL,
  `age` text NOT NULL,
  `gender` text NOT NULL,
  `email` text NOT NULL,
  `doj` text NOT NULL,
  `dob` text NOT NULL,
  `experience` text NOT NULL,
  `proof_id` text NOT NULL,
  `contact` text NOT NULL,
  `address` text NOT NULL,
  `month` text NOT NULL,
  `year` text NOT NULL,
  `basic_salary` text NOT NULL,
  `t_days` text NOT NULL,
  `absent_days` text NOT NULL,
  `medical` text NOT NULL,
  `pf` text NOT NULL,
  `convence` text NOT NULL,
  `net_salary` text NOT NULL,
  `salary_receipt` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp_salary`
--

INSERT INTO `emp_salary` (`e_id`, `Designation`, `name`, `age`, `gender`, `email`, `doj`, `dob`, `experience`, `proof_id`, `contact`, `address`, `month`, `year`, `basic_salary`, `t_days`, `absent_days`, `medical`, `pf`, `convence`, `net_salary`, `salary_receipt`) VALUES
(101, 'Belgavi', 'Nikhil', '21', 'Male', 'nikhilmahendrakar02@gamil.com', '02-03-2023', '02-03-2002', '2', '685567601958', '7019527696', 'Kolli galli beside ZP office Belagavi\n\n\n', 'Dec', '2023', '100000', '30', '4', '2', '5000', '4000', '86094.77', '101.txt');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `emp_salary`
--
ALTER TABLE `emp_salary`
  ADD PRIMARY KEY (`e_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `emp_salary`
--
ALTER TABLE `emp_salary`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
