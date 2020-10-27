CREATE TABLE `news_database`.`personal_details` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email_id` VARCHAR(100) NULL,
  `safe_password` VARCHAR(100) NULL,
  `date_of_birth` DATE NULL,
  `admin_priority` TINYINT NOT NULL,
  `journalist_priority` TINYINT NOT NULL,
  `suscriber_priority` TINYINT NOT NULL,
  `gender` VARCHAR(45) NULL,
  `phone_no` BIGINT(20) NULL,
  `datetimejoined` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP(),
  PRIMARY KEY (`id`, `admin_priority`, `journalist_priority`, `suscriber_priority`));


