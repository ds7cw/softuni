CREATE OR REPLACE PROCEDURE sp_deposit_money(
	account_id INTEGER,
	money_amount NUMERIC(19,4)
)
AS
$$
	BEGIN
		UPDATE accounts
		SET balance = balance + money_amount
		WHERE "id" = account_id;
		
		COMMIT;
	END;
$$
LANGUAGE plpgsql;