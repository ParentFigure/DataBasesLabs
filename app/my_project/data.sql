
DROP SCHEMA IF EXISTS `bookingplatform` ;


CREATE SCHEMA IF NOT EXISTS `bookingplatform` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
SHOW WARNINGS;
USE `bookingplatform` ;

-- -----------------------------------------------------
-- Table `user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `account_status` ENUM('Active', 'Blocked') NULL DEFAULT 'Active',
  `registration_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;
CREATE UNIQUE INDEX `username` ON `user` (`username` ASC) VISIBLE;

SHOW WARNINGS;
CREATE UNIQUE INDEX `email` ON `user` (`email` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `blockedfunds`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `blockedfunds` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `blockedfunds` (
  `blocked_funds_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  `block_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `release_date` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`blocked_funds_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `emailconfirmation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `emailconfirmation` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `emailconfirmation` (
  `confirmation_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `email_sent_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `confirmation_status` ENUM('Confirmed', 'Pending') NULL DEFAULT 'Pending',
  PRIMARY KEY (`confirmation_id`, `user_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `hotelnetwork`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotelnetwork` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `hotelnetwork` (
  `network_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `foundation_year` YEAR NULL DEFAULT NULL,
  PRIMARY KEY (`network_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `location` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `location` (
  `location_id` INT NOT NULL AUTO_INCREMENT,
  `country` VARCHAR(100) NOT NULL,
  `city` VARCHAR(100) NOT NULL,
  `address` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`location_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `hotel`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `hotel` (
  `hotel_id` INT NOT NULL AUTO_INCREMENT,
  `network_id` INT NULL DEFAULT NULL,
  `name` VARCHAR(255) NOT NULL,
  `rating` DECIMAL(3,2) NULL DEFAULT NULL,
  `total_rooms` INT NOT NULL,
  `location_id` INT NOT NULL,
  PRIMARY KEY (`hotel_id`, `location_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `room`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `room` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `room` (
  `room_id` INT NOT NULL AUTO_INCREMENT,
  `hotel_id` INT NOT NULL,
  `room_type` ENUM('Single', 'Double', 'Suite', 'Family') NOT NULL,
  `price_per_night` DECIMAL(10,2) NOT NULL,
  `availability` TINYINT(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`room_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `reservation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `reservation` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `reservation` (
  `reservation_id` INT NOT NULL AUTO_INCREMENT,
  `hotel_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `status` ENUM('Confirmed', 'Cancelled') NULL DEFAULT 'Confirmed',
  `room_id` INT NOT NULL,
  PRIMARY KEY (`reservation_id`, `user_id`, `room_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `payment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `payment` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `payment` (
  `payment_id` INT NOT NULL AUTO_INCREMENT,
  `reservation_id` INT NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  `status` ENUM('Pending', 'Completed', 'Refunded') NULL DEFAULT 'Pending',
  PRIMARY KEY (`payment_id`, `reservation_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

SHOW WARNINGS;
CREATE INDEX `idx_reservation_id_payment` ON `payment` (`reservation_id` ASC) VISIBLE;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Table `review`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `review` ;

CREATE TABLE IF NOT EXISTS `review` (
  `review_id` INT NOT NULL AUTO_INCREMENT,
  `hotel_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `rating` DECIMAL(2,1) NULL DEFAULT NULL,
  `comment` TEXT NULL DEFAULT NULL,
  `review_date` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

-- Insert into `user`
INSERT INTO `user` (user_id, username, email, password, account_status, registration_date) VALUES
(1, 'john_doe', 'john.doe@example.com', 'password123', 'Active', '2024-12-01 10:00:00'),
(2, 'jane_smith', 'jane.smith@example.com', 'securepass', 'Active', '2024-12-02 11:00:00'),
(3, 'admin_user', 'admin@example.com', 'adminpass', 'Blocked', '2024-12-03 12:00:00'),
(4, 'alice', 'alice@example.com', 'alicepass', 'Active', '2024-12-04 13:00:00'),
(5, 'bob', 'bob@example.com', 'bobpass', 'Active', '2024-12-05 14:00:00');

-- Insert into `blockedfunds`
INSERT INTO `blockedfunds` (blocked_funds_id, user_id, amount, block_date, release_date) VALUES
(1, 1, 100.00, '2024-12-01 10:30:00', '2024-12-05 10:30:00'),
(2, 2, 200.00, '2024-12-02 11:30:00', NULL),
(3, 3, 150.50, '2024-12-03 12:30:00', NULL),
(4, 4, 300.00, '2024-12-04 13:30:00', NULL),
(5, 5, 250.00, '2024-12-05 14:30:00', '2024-12-10 14:30:00');

-- Insert into `emailconfirmation`
INSERT INTO `emailconfirmation` (confirmation_id, user_id, email_sent_date, confirmation_status) VALUES
(1, 1, '2024-12-01 10:00:00', 'Confirmed'),
(2, 2, '2024-12-02 11:00:00', 'Pending'),
(3, 3, '2024-12-03 12:00:00', 'Pending'),
(4, 4, '2024-12-04 13:00:00', 'Confirmed'),
(5, 5, '2024-12-05 14:00:00', 'Pending');

-- Insert into `hotelnetwork`
INSERT INTO `hotelnetwork` (network_id, name, description, foundation_year) VALUES
(1, 'Luxury Stays', 'A global network of luxury hotels.', 2000),
(2, 'Budget Inns', 'Affordable stays for travelers.', 1995),
(3, 'Family Resorts', 'Family-friendly accommodations.', 2010),
(4, 'City Lodges', 'Hotels located in urban areas.', 2005),
(5, 'Beachside Villas', 'Villas near popular beaches.', 2015);

-- Insert into `location`
INSERT INTO `location` (location_id, country, city, address) VALUES
(1, 'USA', 'New York', '123 Manhattan Ave'),
(2, 'France', 'Paris', '45 Champs-Elysees'),
(3, 'Japan', 'Tokyo', '10 Shinjuku St'),
(4, 'Italy', 'Rome', '8 Colosseum Rd'),
(5, 'Australia', 'Sydney', '20 Opera House Ln');

-- Insert into `hotel`
INSERT INTO `hotel` (hotel_id, network_id, name, rating, total_rooms, location_id) VALUES
(1, 1, 'Manhattan Luxury Hotel', 4.8, 200, 1),
(2, 2, 'Paris Budget Inn', 3.5, 150, 2),
(3, 3, 'Tokyo Family Resort', 4.2, 180, 3),
(4, 4, 'Rome City Lodge', 4.0, 100, 4),
(5, 5, 'Sydney Beachside Villa', 4.7, 120, 5);

-- Insert into `room`
INSERT INTO `room` (room_id, hotel_id, room_type, price_per_night, availability) VALUES
(1, 1, 'Single', 100.00, 1),
(2, 1, 'Double', 150.00, 1),
(3, 2, 'Single', 80.00, 1),
(4, 3, 'Suite', 300.00, 1),
(5, 4, 'Family', 200.00, 1);

-- Insert into `reservation`
INSERT INTO `reservation` (reservation_id, hotel_id, user_id, start_date, end_date, status, room_id) VALUES
(1, 1, 1, '2024-12-15', '2024-12-20', 'Confirmed', 1),
(2, 2, 2, '2024-12-16', '2024-12-18', 'Cancelled', 2),
(3, 3, 3, '2024-12-19', '2024-12-22', 'Confirmed', 3),
(4, 4, 4, '2024-12-20', '2024-12-25', 'Confirmed', 4),
(5, 5, 5, '2024-12-21', '2024-12-24', 'Confirmed', 5);

-- Insert into `payment`
INSERT INTO `payment` (payment_id, reservation_id, amount, status) VALUES
(1, 1, 500.00, 'Completed'),
(2, 2, 300.00, 'Pending'),
(3, 3, 800.00, 'Completed'),
(4, 4, 1000.00, 'Refunded'),
(5, 5, 750.00, 'Completed');

-- Insert into `review`
INSERT INTO `review` (review_id, hotel_id, user_id, rating, comment, review_date) VALUES
(1, 1, 1, 4.5, 'Great experience!', '2024-12-05 12:00:00'),
(2, 2, 2, 3.0, 'Average stay.', '2024-12-06 13:00:00'),
(3, 3, 3, 4.8, 'Highly recommend!', '2024-12-07 14:00:00'),
(4, 4, 4, 4.0, 'Good service.', '2024-12-08 15:00:00'),
(5, 5, 5, 4.7, 'Beautiful location.', '2024-12-09 16:00:00');


SELECT 
    location.city AS City,
    CONCAT(user.username, ' (', user.email, ')') AS UserInfo
FROM 
    location
LEFT JOIN 
    user ON location.location_id = user.user_id
ORDER BY 
    location.city, user.username;
    

SELECT 
    hotel.name AS HotelName,
    CONCAT(user.username, ' (', user.email, ')') AS UserInfo
FROM 
    reservation
JOIN 
    hotel ON reservation.hotel_id = hotel.hotel_id
JOIN 
    user ON reservation.user_id = user.user_id
ORDER BY 
    hotel.name, user.username;


-- lab 5 

CREATE TABLE IF NOT EXISTS user_logs (
    log_id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL,
    action VARCHAR(50) NOT NULL,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (log_id)
);

DELIMITER $$
CREATE TRIGGER log_new_user
AFTER INSERT ON user
FOR EACH ROW
BEGIN
    INSERT INTO user_logs (user_id, username, email, action)
    VALUES (NEW.user_id, NEW.username, NEW.email, 'User Added');
END$$
DELIMITER ;

-- INSERT INTO user (username, email, password, account_status) 
-- VALUES ('new_user', 'new_user@example.com', 'securepass', 'Active');

-- SELECT * FROM user_logs;


DELIMITER $$
CREATE PROCEDURE insert_new_user(
    IN p_username VARCHAR(100),
    IN p_email VARCHAR(255),
    IN p_password VARCHAR(255),
    IN p_account_status VARCHAR(10)
)
BEGIN
    -- Перевіряємо, чи вказаний статус є допустимим
    IF p_account_status NOT IN ('Active', 'Blocked') THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Invalid account status. Allowed values: Active, Blocked';
    END IF;

    -- Перевіряємо, чи вже існує користувач з таким ім'ям або email
    IF EXISTS (SELECT 1 FROM user WHERE username = p_username OR email = p_email) THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'User with this username or email already exists';
    ELSE
        -- Додаємо нового користувача
        INSERT INTO user (username, email, password, account_status)
        VALUES (p_username, p_email, p_password, p_account_status);
    END IF;
END$$
DELIMITER ;

-- CALL insert_new_user('example_user', 'example_user@example.com', 'secure_password', 'Active');

DELIMITER $$
CREATE FUNCTION user_exists(p_username VARCHAR(100), p_email VARCHAR(255))
RETURNS TINYINT
DETERMINISTIC
BEGIN
    DECLARE user_count INT;

    SELECT COUNT(*) INTO user_count
    FROM user
    WHERE username = p_username OR email = p_email;

    IF user_count > 0 THEN
        RETURN 1;
    ELSE
        RETURN 0;
    END IF;
END$$
DELIMITER ;


-- SELECT user_exists('example_user', 'example_user@example.com') AS UserExists;

DELIMITER $$
CREATE PROCEDURE distribute_users_to_tables()
BEGIN
    -- Оголошення змінних
    DECLARE finished INT DEFAULT 0;
    DECLARE current_user_id INT;
    DECLARE current_username VARCHAR(100);
    DECLARE current_email VARCHAR(255);

    -- Оголошення курсора
    DECLARE user_cursor CURSOR FOR
        SELECT user_id, username, email FROM user;

    -- Оголошення обробника для кінця курсора
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;

    -- Унікальні імена для нових таблиць
    SET @table1_name = CONCAT('user_table1_', UNIX_TIMESTAMP());
    SET @table2_name = CONCAT('user_table2_', UNIX_TIMESTAMP());

    -- Динамічне створення нових таблиць
    SET @create_table1 = CONCAT(
        'CREATE TABLE ', @table1_name, ' LIKE user'
    );
    SET @create_table2 = CONCAT(
        'CREATE TABLE ', @table2_name, ' LIKE user'
    );

    PREPARE stmt1 FROM @create_table1;
    EXECUTE stmt1;
    DEALLOCATE PREPARE stmt1;

    PREPARE stmt2 FROM @create_table2;
    EXECUTE stmt2;
    DEALLOCATE PREPARE stmt2;

    -- Відкриття курсора
    OPEN user_cursor;

    -- Цикл для ітерації по курсору
    read_loop: LOOP
        FETCH user_cursor INTO current_user_id, current_username, current_email;
        IF finished THEN
            LEAVE read_loop;
        END IF;

        -- Випадковий вибір таблиці
        IF RAND() > 0.5 THEN
            SET @insert_query = CONCAT(
                'INSERT INTO ', @table1_name, 
                ' (user_id, username, email, password, account_status, registration_date) ',
                'SELECT user_id, username, email, password, account_status, registration_date FROM user WHERE user_id = ', current_user_id
            );
        ELSE
            SET @insert_query = CONCAT(
                'INSERT INTO ', @table2_name, 
                ' (user_id, username, email, password, account_status, registration_date) ',
                'SELECT user_id, username, email, password, account_status, registration_date FROM user WHERE user_id = ', current_user_id
            );
        END IF;

        PREPARE stmt FROM @insert_query;
        EXECUTE stmt;
        DEALLOCATE PREPARE stmt;
    END LOOP;

    -- Закриття курсора
    CLOSE user_cursor;

    -- Повідомлення про успішне виконання
    SELECT CONCAT('Data distributed to tables: ', @table1_name, ' and ', @table2_name) AS message;
END$$
DELIMITER ;



-- CALL distribute_users_to_tables();

