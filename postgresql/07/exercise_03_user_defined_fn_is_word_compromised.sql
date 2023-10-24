CREATE OR REPLACE FUNCTION fn_is_word_comprised(
	IN set_of_letters VARCHAR(50),
	IN word VARCHAR(50),
	OUT is_compromised BOOLEAN
) AS
$$
	BEGIN
		set_of_letters := LOWER(TRANSLATE(set_of_letters, '!@#$%^&*(){}[]<>,.|\/?_-=+ ', ''));
		word := LOWER(TRANSLATE(word, '!@#$%^&*(){}[]<>,.|\/?_-=+ ', ''));		
	
		is_compromised := TRIM(word, set_of_letters) = '';
	END;
$$
LANGUAGE plpgsql;