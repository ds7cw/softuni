CREATE OR REPLACE PROCEDURE sp_withdraw_money(
	account_id INTEGER,
	money_amount NUMERIC(19,4)
) AS
$$
	BEGIN

		
		IF (SELECT balance FROM accounts WHERE id = account_id) - money_amount < 0 THEN
			RAISE NOTICE '% %', 'Insufficient balance to withdraw', money_amount;
		ELSE
				UPDATE accounts
				SET balance = balance - money_amount
				WHERE id = account_id;
		END IF;
		COMMIT;
	END;
$$
LANGUAGE plpgsql;