CREATE FUNCTION convert_custom_time(input VARCHAR(10)) RETURNS TIME
DETERMINISTIC
BEGIN
    DECLARE h INT;
    DECLARE m_decimal DECIMAL(5,2);
    DECLARE total_seconds INT;

    SET h = FLOOR(SUBSTRING_INDEX(input, ':', 1));
    SET m_decimal = CAST(SUBSTRING_INDEX(input, ':', -1) AS DECIMAL(5,2));

    SET total_seconds = h * 3600 + FLOOR(m_decimal) * 60 + ROUND((m_decimal - FLOOR(m_decimal)) * 60);

    RETURN SEC_TO_TIME(total_seconds);
END;


