-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Янв 09 2026 г., 21:04
-- Версия сервера: 8.0.30
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `shop`
--

-- --------------------------------------------------------

--
-- Структура таблицы `products`
--

CREATE TABLE `products` (
  `ID` int NOT NULL,
  `name` varchar(24) NOT NULL,
  `category` varchar(24) NOT NULL,
  `price` int NOT NULL,
  `remains` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `products`
--

INSERT INTO `products` (`ID`, `name`, `category`, `price`, `remains`) VALUES
(1, 'Pepsi', 'Drinks', 3, 29),
(2, 'Fanta', 'Drinks', 2, 30),
(3, 'Coca-cola', 'Drinks', 4, 35),
(4, 'Sukkiri', 'Drinks', 4, 20),
(5, 'Betty Tonic', 'Drinks', 2, 35),
(6, 'Mirinda', 'Drinks', 1, 20),
(8, 'Pringles', 'Snacks', 5, 52),
(9, 'Oreo', 'Snacks', 3, 13),
(10, 'Lays', 'Snacks', 2, 32),
(11, 'Cerveza', 'Alcohol', 1, 29),
(12, 'Funchon', 'Alcohol', 4, 19),
(13, 'Amsterdamer', 'Alcohol', 5, 58),
(14, 'Whiskey', 'Alcohol', 3, -1),
(15, 'Sheffon Light', 'Alcohol', 1, 14),
(16, 'Sheffon', 'Alcohol', 2, 27),
(17, 'Jummy Strong', 'Cigarettes', 8, 40),
(18, 'Spade', 'Cigarettes', 10, 15),
(19, 'Super Blend', 'Cigarettes', 12, 27),
(20, 'Premium Tobacco', 'Cigarettes', 15, 55),
(21, 'Super Blend Strong', 'Cigarettes', 8, 20),
(22, 'Old Bow Hat', 'Hats', 20, 40),
(23, 'Drago Red Hat', 'Hats', 9, 11),
(24, 'Cowboy Hat', 'Hats', 14, 11),
(25, 'Fake Police Hat', 'Hats', 8, 23),
(26, 'Viking Hornless Hat', 'Hats', 25, 0),
(27, 'Runcher Hat', 'Hats', 10, 40),
(28, 'Aviator Glasses', 'Glasses', 5, 20),
(29, 'Cool Glasses', 'Glasses', 3, 15),
(30, 'Vintage Glasses', 'Glasses', 17, 50),
(31, 'Cateye Glasses', 'Glasses', 20, 30),
(32, 'Chocolate Glasses', 'Glasses', 10, 25),
(33, 'Teashade Glasses', 'Glasses', 8, 10),
(34, 'Armadilo Plush', 'Plush toys', 9, 19),
(35, 'Dog Plush', 'Plush toys', 8, 20),
(36, 'Teddy Plush', 'Plush toys', 20, 13),
(37, 'Vampig', 'Plush toys', 25, 29),
(38, 'Zebra Toy', 'Toys', 9, 25),
(39, 'Bear Toy', 'Toys', 11, 20),
(40, 'Car Toy', 'Toys', 5, 25),
(41, 'Girrafe Toy', 'Toys', 15, 9),
(42, 'Worm Toy', 'Toys', 9, 20),
(43, 'R35', 'Toys', 40, 30),
(44, 'Chocolate Donut', 'Donuts', 4, 30),
(45, 'Strawberry Donut', 'Donuts', 3, 30),
(46, 'Cream Donut', 'Donuts', 2, 15),
(47, 'Morning Donut', 'Donuts', 2, 30),
(48, 'Time', 'Papers', 1, 24),
(49, 'Boham Daily', 'Papers', 2, 44),
(50, 'The Sport', 'Papers', 1, 29),
(51, 'Puzzles', 'Papers', 3, 67),
(52, 'Home Cooking', 'Papers', 2, 30),
(53, 'News', 'Papers', 1, 10),
(54, 'Bold Almond', 'Ice Cream', 2, 30),
(55, 'Freshetta Milk', 'Ice Cream', 1, 20),
(56, 'Rainbow Stick', 'Ice Cream', 1, 20),
(57, 'Frooty', 'Ice Cream', 2, 15),
(58, 'Freshetta Cocoa', 'Ice Cream', 2, 15);

-- --------------------------------------------------------

--
-- Структура таблицы `sellingHystory`
--

CREATE TABLE `sellingHystory` (
  `ID` int NOT NULL,
  `customerID` int DEFAULT NULL,
  `productName` varchar(24) DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `categoryName` varchar(24) DEFAULT NULL,
  `transactionTime` datetime DEFAULT CURRENT_TIMESTAMP,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `sellingHystory`
--

INSERT INTO `sellingHystory` (`ID`, `customerID`, `productName`, `quantity`, `categoryName`, `transactionTime`, `price`) VALUES
(1, 1, 'Pringles', 2, NULL, '2026-01-06 19:32:26', 10),
(2, 1, 'Oreo', 2, NULL, '2026-01-06 19:32:26', 6),
(3, 1, 'Lays', 2, NULL, '2026-01-06 19:32:26', 4),
(4, 1, 'Viking Hornless Hat', 2, NULL, '2026-01-06 19:32:26', 50),
(5, 1, 'Fake Police Hat', 2, NULL, '2026-01-06 19:32:26', 16),
(6, 1, 'Cowboy Hat', 1, NULL, '2026-01-06 19:32:26', 14),
(7, 1, 'Girrafe Toy', 1, 'Unknown', '2026-01-06 19:34:11', 15),
(8, 1, 'Super Blend', 1, 'Cigarettes', '2026-01-06 19:39:59', 12),
(9, 1, 'Super Blend', 1, 'Cigarettes', '2026-01-06 19:40:13', 12),
(10, 1, 'Armadilo Plush', 1, 'Plush toys', '2026-01-06 19:40:13', 9),
(11, 1, 'Teddy Plush', 2, 'Plush toys', '2026-01-06 19:40:13', 40),
(12, 1, 'Vampig', 1, 'Plush toys', '2026-01-06 19:40:13', 25),
(13, 1, 'Puzzles', 3, 'Papers', '2026-01-06 19:40:13', 9),
(14, 1, 'Boham Daily', 1, 'Papers', '2026-01-06 19:40:13', 2),
(15, 1, 'The Sport', 1, 'Papers', '2026-01-06 19:40:13', 1),
(16, 1, 'Time', 1, 'Papers', '2026-01-06 19:40:13', 1),
(17, 4, 'Whiskey', 7, 'Alcohol', '2026-01-06 19:42:36', 21),
(18, 4, 'Amsterdamer', 2, 'Alcohol', '2026-01-06 19:42:36', 10),
(19, 4, 'Funchon', 1, 'Alcohol', '2026-01-06 19:42:36', 4),
(20, 4, 'Cerveza', 1, 'Alcohol', '2026-01-06 19:42:36', 1),
(21, 4, 'Sheffon Light', 1, 'Alcohol', '2026-01-06 19:42:36', 1),
(22, 4, 'Sheffon', 3, 'Alcohol', '2026-01-06 19:42:36', 6),
(23, 4, 'Whiskey', 4, 'Alcohol', '2026-01-06 19:43:24', 12),
(24, 1, 'Pringles', 3, 'Snacks', '2026-01-06 19:45:06', 15),
(25, 1, 'Oreo', 1, 'Snacks', '2026-01-06 19:45:06', 3),
(26, 1, 'Pringles', 1, 'Snacks', '2026-01-06 19:45:39', 5),
(27, 1, 'Oreo', 2, 'Snacks', '2026-01-06 19:45:39', 6),
(28, 1, 'Lays', 1, 'Snacks', '2026-01-06 19:45:39', 2),
(29, 1, 'Pringles', 2, 'Snacks', '2026-01-06 19:47:23', 10),
(30, 1, 'Oreo', 2, 'Snacks', '2026-01-06 19:47:23', 6),
(31, 3, 'Viking Hornless Hat', 8, 'Hats', '2026-01-06 19:57:02', 200),
(32, 1, 'Super Blend', 1, 'Cigarettes', '2026-01-09 20:41:24', 12);

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `ID` int NOT NULL,
  `username` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `registration_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `balance` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`ID`, `username`, `password`, `registration_date`, `balance`) VALUES
(1, 'naz', '0000', '2026-01-06 18:58:23', 9714),
(3, 'Nazar', '1111', '2026-01-06 18:59:38', 24),
(4, 'Final Test', 'Nine9_$', '2026-01-06 19:41:56', 45),
(5, '21314', '21314', '2026-01-09 21:00:25', 0);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Индексы таблицы `sellingHystory`
--
ALTER TABLE `sellingHystory`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `products`
--
ALTER TABLE `products`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT для таблицы `sellingHystory`
--
ALTER TABLE `sellingHystory`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `ID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
