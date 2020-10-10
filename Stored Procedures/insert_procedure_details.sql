CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_personal_details`(
IN first_name1 varchar(100),
IN last_name1 varchar(100),
IN email_id1 varchar(100),
IN password1 varchar(100),
IN dateofbirth1 date
)
BEGIN



    DECLARE errno INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
    GET CURRENT DIAGNOSTICS CONDITION 1 errno = MYSQL_ERRNO;
    SELECT errno AS MYSQL_ERROR;
    ROLLBACK;
    END;

    START TRANSACTION;
INSERT INTO authentication_personaldetails (
first_name,
last_name,
email_id,
password,
date_of_birth)
    VALUES (first_name1
    , last_name1
    , email_id1
    , password1
    , dateofbirth1);


      COMMIT WORK;

END