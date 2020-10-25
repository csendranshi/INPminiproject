-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 25, 2020 at 01:34 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `news_database`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_personal_details` (IN `first_name` VARCHAR(200), IN `last_name` VARCHAR(200), IN `email_id` VARCHAR(200), IN `safe_password` VARCHAR(200), IN `dateofbirth` DATE, IN `gender` VARCHAR(100), IN `phone_no` BIGINT)  MODIFIES SQL DATA
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
INSERT INTO personal_details (
first_name,
last_name,
email_id,
safe_password,
date_of_birth,
gender,
phone_no)
    VALUES (first_name
    , last_name
    , email_id
    , safe_password
    , dateofbirth,
      gender,
      phone_no);
    
    
      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `latest_top_stories` (IN `title` MEDIUMTEXT, IN `image` LONGTEXT, IN `image_link` MEDIUMTEXT, IN `content` LONGTEXT, IN `useremailid` VARCHAR(100), IN `category` VARCHAR(100), IN `section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
INSERT INTO top_stories (
title,
image,
image_link,
content,
user_email_id,
category,
section,
news_unique_id)
    VALUES (title
    , image
    , image_link
    , content
    , useremailid
    , category
    , section
    , news_unique_id);    
      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_business_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE business_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_education_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE education_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_health_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE health_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_india_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE india_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_latest_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE latest_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_technology_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE technology_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `update_world_grid` (IN `in_title` MEDIUMTEXT, IN `in_image` LONGTEXT, IN `in_image_link` MEDIUMTEXT, IN `in_content` LONGTEXT, IN `in_useremailid` VARCHAR(100), IN `in_category` VARCHAR(100), IN `in_section` VARCHAR(100), IN `news_unique_id` INT)  NO SQL
BEGIN
    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;
    START TRANSACTION;
UPDATE world_grid SET title=in_title, image = in_image,
image_link =in_image_link,
content=in_content,
user_email_id=in_useremailid,
category=in_category,
section=in_section,
news_unique_id=news_unique_id,
datetime=current_timestamp()
where id=in_section;

      COMMIT WORK;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `verify_email_id` (IN `email_id_in` VARCHAR(100), OUT `STATUS1` VARCHAR(100))  MODIFIES SQL DATA
BEGIN
	DECLARE email varchar(100) DEFAULT '';
	select email_id INTO email
    from personal_details 
    where email_id=email_id_in;
    
    IF email_id_in = email THEN
		SET STATUS1 = 'EMAIL ID TAKEN';
	ELSE
		SET STATUS1 = 'EMAIL ID NOT TAKEN';
	END IF;
        
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-10-11 12:11:33.948717'),
(2, 'auth', '0001_initial', '2020-10-11 12:11:41.539726'),
(3, 'admin', '0001_initial', '2020-10-11 12:12:20.471592'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-10-11 12:12:29.258513'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-10-11 12:12:29.486875'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-10-11 12:12:33.173913'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-10-11 12:12:36.515309'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-10-11 12:12:36.760681'),
(9, 'auth', '0004_alter_user_username_opts', '2020-10-11 12:12:36.840151'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-10-11 12:12:39.429945'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-10-11 12:12:39.526684'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-10-11 12:12:39.609435'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-10-11 12:12:39.756043'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-10-11 12:12:39.944567'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-10-11 12:12:40.126053'),
(16, 'auth', '0011_update_proxy_permissions', '2020-10-11 12:12:40.217808'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2020-10-11 12:12:40.767015'),
(18, 'authentication', '0001_initial', '2020-10-11 12:12:42.325574'),
(19, 'authentication', '0002_auto_20201008_0840', '2020-10-11 12:12:46.074585'),
(20, 'authentication', '0003_auto_20201008_0844', '2020-10-11 12:12:46.144047'),
(21, 'authentication', '0004_auto_20201008_0852', '2020-10-11 12:12:52.861742'),
(22, 'authentication', '0005_auto_20201008_0912', '2020-10-11 12:12:53.011197'),
(23, 'authentication', '0006_auto_20201008_0912', '2020-10-11 12:12:53.221750'),
(24, 'authentication', '0007_auto_20201008_0917', '2020-10-11 12:12:54.545153'),
(25, 'authentication', '0008_auto_20201009_0419', '2020-10-11 12:12:55.143701'),
(26, 'authentication', '0009_delete_personaldetails', '2020-10-11 12:12:55.751110'),
(27, 'sessions', '0001_initial', '2020-10-11 12:12:56.616330');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0s3pd7uuv2hm6ouc174hy6xrnge8vp2y', '.eJxdzkEKwjAQheG7zLoIdZeuBG_gBcI0mcaRZEYmyULEu1tdVOr2g__xnpA1JYqeBaYFc6UBbtpNMHsMgWrdGGNh-ceFrTYvWAgmuFCfSWCAjD88a28sV1259hqMZzJ_N1bj9th2qCBnz3EN7LtyHEfn3Cl9_BC07PLdidcbBItF9Q:1kSYRT:niJo1RecPfdQiWG7aaV_SmANTRCtoJKBOKBn7M5hkyw', '2020-10-28 04:31:11.767700'),
('hk4fo4tgcg9z6bo0ugism6hhse4289h0', '.eJxFykEKAjEMAMC_5LwI6617EvyBHyjZNlsjbSpJexDx71Zh9TrME3JNiaJngaVppwlutatg9hgCme2KsbD8bMNsA61bUF5J_V25KrfH3jdWa16wECxwob6SwAQZ_3iuvbFc62AqyNlzHKrfepxn59wpffwQaoHXGzmFO7w:1kVv4r:SXvavYeEBHraa-U6JUJNq7PKffT9QVKzjntO68-EgL0', '2020-11-06 11:17:45.163582');

-- --------------------------------------------------------

--
-- Table structure for table `personal_details`
--

CREATE TABLE `personal_details` (
  `idpersonal_details` int(11) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email_id` varchar(100) DEFAULT NULL,
  `safe_password` varchar(100) DEFAULT NULL,
  `date_of_birth` varchar(100) DEFAULT NULL,
  `admin_priority` tinyint(4) DEFAULT 0,
  `journalist_priority` tinyint(4) DEFAULT 0,
  `suscriber_priority` tinyint(1) NOT NULL DEFAULT 1,
  `gender` varchar(100) NOT NULL,
  `phone_no` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `personal_details`
--

INSERT INTO `personal_details` (`idpersonal_details`, `first_name`, `last_name`, `email_id`, `safe_password`, `date_of_birth`, `admin_priority`, `journalist_priority`, `suscriber_priority`, `gender`, `phone_no`) VALUES
(3, 'Reuben', 'Coutinho', 'reuben211999@gmail.com', 'sha256$269Weu3G$1dcd536a61e4451d25135549689879c39353b55f6568e5ed3e5ba9881ea8d351', '2020-10-21', 0, 1, 1, 'Male', 7021597154),
(13, 'Reuben', 'Coutinho', 'reuben21@gmail.com', 'sha256$ah0IJ6i7$6b33db3b30b7b41affc7cb7c05297d5ed1583ee6ab0be14b44ab186e9a77897b', '2020-10-20', 0, 0, 1, 'Male', 8291310013);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `personal_details`
--
ALTER TABLE `personal_details`
  ADD PRIMARY KEY (`idpersonal_details`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `personal_details`
--
ALTER TABLE `personal_details`
  MODIFY `idpersonal_details` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
