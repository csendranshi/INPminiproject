CREATE DEFINER=`root`@`localhost` PROCEDURE `verify_email_id`(
IN email_id_in varchar(100),
OUT STATUS1 varchar(100)
)
BEGIN
	DECLARE email varchar(100) DEFAULT '';
	select email_id INTO email
    from authentication_personaldetails
    where email_id=email_id_in;

    IF email_id_in = email THEN
		SET STATUS1 = 'EMAIL ID TAKEN';
	ELSE
		SET STATUS1 = 'EMAIL ID NOT TAKEN';
	END IF;

END